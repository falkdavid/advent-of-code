from queue import Queue, Empty
from typing import List

class IntcodeComputer(object):

    num_parameters = {
        1:3,   2:3,   3:1,   4:1,
        5:2,   6:2,   7:3,   8:3,
        99:0
    }

    def __init__(self):
        self.mem = []
        self.isp = 0

        self.inps = Queue()
        self.outs = Queue()

        self.running = False

        self.instructions = {
            1:self.add, 2:self.mul, 3:self.inn, 4:self.out,
            5:self.jtr, 6:self.jfa, 7:self.slt, 8:self.seq
        }

    """
        Instructions
    """

    # Add p3 = p1 + p2  
    def add(self, *args):
        vp1, vp2, vp3, p1, p2, p3 = args
        self.set_ptr(p3, vp1 + vp2)
        self.isp += 4

    # Add p3 = p1 * p2
    def mul(self, *args):
        vp1, vp2, vp3, p1, p2, p3 = args
        self.set_ptr(p3, vp1 * vp2)
        self.isp += 4

    # p1 = input()
    def inn(self, *args):
        vp1, p1 = args
        val = self.inps.get_nowait()
        self.set_ptr(p1, val)
        self.isp += 2

    # Output p1
    def out(self, *args):
        vp1, p1 = args
        self.outs.put_nowait(vp1)
        self.isp += 2

    # isp = p2 if p1 != 0
    def jtr(self, *args):
        vp1, vp2, p1, p2 = args
        if vp1 != 0:
            self.isp = vp2
        else:
            self.isp += 3

    # isp = p2 if p1 == 0
    def jfa(self, *args):
        vp1, vp2, p1, p2 = args
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

        self.isp += 4

    # p3 = 1 if p1 == p2 else 0
    def seq(self, *args):
        vp1, vp2, vp3, p1, p2, p3 = args
        if vp1 == vp2:
            self.set_ptr(p3, 1)
        else:
            self.set_ptr(p3, 0)

        self.isp += 4

    """
        Methods
    """

    def set_ptr(self, addr, value):
        self.mem[addr] = value 

    def get_ptr(self, addr):
        return self.mem[addr]

    def get_para_values(self, op, modes):
        values = []
        for i in range(self.num_parameters[op]):
            mode = modes[i]
            if mode == 0:
                values.append(self.mem[self.mem[self.isp+i+1]])
            elif mode == 1:
                values.append(self.mem[self.isp+i+1])
        
        return values

    def get_paras(self, op):
        paras = []
        for i in range(self.num_parameters[op]):
            paras.append(self.mem[self.isp+i+1])
        return paras

    def exec(self, *args):
        try:
            op = args[0]
            arg_list = []
            arg_list.extend(self.get_para_values(op, args[1:]))
            arg_list.extend(self.get_paras(op))
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
            #print(op, modes)
        except KeyError as e:
            print(e)
            self.running = False
            return

        if op == 99:
            self.running = False
            return
        try:
            self.exec(op, *modes)
        except Exception as e:
            #print(e)
            self.running = False
            return

        #print(self.mem)


    def run(self, prog, inps):
        self.isp = 0

        self.load_prog(prog)
        self.put_inputs(inps)
        
        self.running = True
        while self.running:
            self.exec_next()

        return self.get_outputs()

if __name__ == "__main__":

    cpu = IntcodeComputer()
    prog = list(map(int, "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(',')))
    assert cpu.run(prog, [10])[0] == 1001
    assert cpu.run(prog, [8])[0] == 1000
    assert cpu.run(prog, [7])[0] == 999
    print("Passed!")
