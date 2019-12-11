from queue import Queue, Empty
from typing import List

class IntcodeComputer(object):

    num_parameters = {
        1:3,   2:3,   3:1,   4:1,
        5:2,   6:2,   7:3,   8:3,
        9:1,  99:0
    }

    def __init__(self, debug=False):
        self.mem = []
        self.isp = 0
        self.rel_base = 0

        self.inps = Queue()
        self.outs = Queue()

        self.running = False
        self.debug = debug

        self.instructions = {
            1:self.add, 2:self.mul, 3:self.inn, 4:self.out,
            5:self.jtr, 6:self.jfa, 7:self.slt, 8:self.seq,
            9:self.srb,99:self.hlt
        }

    """
        Instructions
    """

    # Add p3 = p1 + p2  
    def add(self, *args):
        vp1, vp2, vp3, p1, p2, p3 = args
        self.set_ptr(p3, vp1 + vp2)
        if self.debug: print(f"(${self.isp})\tADD: ${p3}({self.get_ptr(p3)}) = ${p1}({vp1}) + ${p2}({vp2})")
        self.isp += 4

    # Add p3 = p1 * p2
    def mul(self, *args):
        vp1, vp2, vp3, p1, p2, p3 = args
        self.set_ptr(p3, vp1 * vp2)
        if self.debug: print(f"(${self.isp})\tMUL: ${p3}({self.get_ptr(p3)}) = ${p1}({vp1}) * ${p2}({vp2})")
        self.isp += 4

    # p1 = input()
    def inn(self, *args):
        vp1, p1 = args
        val = self.inps.get_nowait()
        if self.debug: print(f"(${self.isp})\tINN: ${p1} = {val}")
        self.set_ptr(p1, val)
        self.isp += 2

    # Output p1
    def out(self, *args):
        vp1, p1 = args
        self.outs.put_nowait(vp1)
        if self.debug: print(f"(${self.isp})\tOUT: {vp1}")
        self.isp += 2

    # isp = p2 if p1 != 0
    def jtr(self, *args):
        vp1, vp2, p1, p2 = args
        if self.debug: print(f"(${self.isp})\tJTR: ? ${p1}({vp1}) != 0: isp={vp2 if vp1 != 0 else self.isp + 3}")
        if vp1 != 0:
            self.isp = vp2
        else:
            self.isp += 3

    # isp = p2 if p1 == 0
    def jfa(self, *args):
        vp1, vp2, p1, p2 = args
        if self.debug: print(f"(${self.isp})\tJFA: ? ${p1}({vp1}) == 0: isp={vp2 if vp1 == 0 else self.isp + 3}")
        if vp1 == 0:
            self.isp = vp2
        else:
            self.isp += 3
    
    # p3 = 1 if p1 < p2 else 0
    def slt(self, *args):
        vp1, vp2, vp3, p1, p2, p3 = args
        if vp1 < vp2:
            self.set_ptr(p3, 1)
        else:
            self.set_ptr(p3, 0)

        if self.debug: print(f"(${self.isp})\tSLT: ? ${p1}({vp1}) < ${p2}({vp2}): ${p3}={self.get_ptr(p3)}")
        self.isp += 4

    # p3 = 1 if p1 == p2 else 0
    def seq(self, *args):
        vp1, vp2, vp3, p1, p2, p3 = args
        if vp1 == vp2:
            self.set_ptr(p3, 1)
        else:
            self.set_ptr(p3, 0)

        if self.debug: print(f"(${self.isp})\tSEQ: ? ${p1}({vp1}) == ${p2}({vp2}): ${p3}={self.get_ptr(p3)}")
        self.isp += 4

    # rel_base = p1
    def srb(self, *args):
        vp1, p1 = args
        self.rel_base += vp1
        if self.debug: print(f"(${self.isp})\tSRB: re_base={self.rel_base}")
        self.isp += 2
        
    # running = False
    def hlt(self, *args):
        if self.debug: print(f"(${self.isp})\tHLT")
        self.running = False

    """
        Methods
    """

    def set_ptr(self, addr, value):
        if addr < 0:
            #raise RuntimeError("Cannot write to negative Address!")
            return
        if addr >= len(self.mem):
            new_mem = addr - len(self.mem) + 1
            self.mem.extend([0]*(new_mem))
        self.mem[addr] = value 

    def get_ptr(self, addr):
        if addr < 0:
            #raise RuntimeError("Cannot read negative Address!")
            return None
        if addr >= len(self.mem):
            new_mem = addr - len(self.mem) + 1
            self.mem.extend([0]*(new_mem))
        return self.mem[addr]

    def get_para_values(self, op, modes):
        values = []
        for i in range(self.num_parameters[op]):
            mode = modes[i]
            para_addr = self.isp + i + 1
            if mode == 0:
                para = self.mem[para_addr]
                values.append(self.get_ptr(para))
            elif mode == 1:
                para = self.mem[para_addr]
                values.append(para)
            elif mode == 2:
                addr = self.rel_base + self.mem[para_addr]
                values.append(self.get_ptr(addr))
        return values

    def get_paras(self, op, modes):
        paras = []
        for i in range(self.num_parameters[op]):
            mode = modes[i]
            para_addr = self.isp + i + 1
            if mode == 0:
                paras.append(self.mem[para_addr])
            elif mode == 1:
                paras.append(self.mem[para_addr])
            elif mode == 2:
                paras.append(self.rel_base + self.mem[para_addr])
        return paras

    def exec(self, *args):
        try:
            op = args[0]
            modes = args[1:]
            arg_list = []
            arg_list.extend(self.get_para_values(op, modes))
            arg_list.extend(self.get_paras(op, modes))
            #print(f"arg_list: {arg_list}")
            self.instructions[op](*arg_list)
        except KeyError as e:
            raise RuntimeError(f"No such instruction {op}!")
        except:
            raise

    def put_input(self, data):
        self.inps.put_nowait(data)

    def put_inputs(self, data: List):
        for d in data:
            self.inps.put_nowait(d)

    def get_output(self):
        if not self.outs.empty():
            return self.outs.get_nowait()
        return None

    def get_outputs(self):
        outs = []
        while not self.outs.empty():
            outs.append(self.outs.get())
        return outs

    def load_prog(self, prog):
        self.mem = prog[:]

    def fetch_instr(self):
        instr = self.mem[self.isp]
        op = instr % 100
        modes = []
        i = 100
        for _ in range(self.num_parameters[op]):
            modes.append(instr // i % 10) 
            i *= 10

        return op, tuple(modes)

    def exec_next(self):
        try:
            op, modes = self.fetch_instr()
            self.exec(op, *modes)
        except KeyError as e:
            print("Unknown instruction!")
            print(e)
            self.running = False
            return
        except Exception as e:
            print(e)
            self.running = False
            return

        #print(self.mem)

    def exec_until_output(self, num=1):
        outs = []
        while len(outs) < num:
            if self.running:
                self.exec_next()
                out = self.get_output()
                if out is not None:
                    outs.append(out)
            else:
                break
        return outs

    def init(self):
        self.isp = 0
        self.rel_base = 0

    def run(self, prog, inps=[]):
        self.init()

        self.load_prog(prog)
        self.put_inputs(inps)
        
        self.running = True
        while self.running:
            self.exec_next()

        return self.get_outputs()

if __name__ == "__main__":

    cpu = IntcodeComputer(debug=True)
    print("Doing some tests...")

    # test greater than, less than and equal to 8
    print("Test: Input greater than, less than or equal to 8")
    prog = list(map(int, "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(',')))
    assert cpu.run(prog, [10])[0] == 1001
    assert cpu.run(prog, [8])[0] == 1000
    assert cpu.run(prog, [7])[0] == 999

    # produce copy of itself
    print("Test: copy of itself")
    prog = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    assert cpu.run(prog) == prog

    print("Test: Output digit length")
    prog = [1102,34915192,34915192,7,4,7,99,0]
    assert len(str(cpu.run(prog)[0])) == 16

    print("Test: Output value")
    prog = [104,1125899906842624,99]
    assert cpu.run(prog)[0] == 1125899906842624
    print("Passed!")
