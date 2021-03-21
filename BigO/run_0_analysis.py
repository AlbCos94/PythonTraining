from BigO import BigO as bo
from BigO import BigO_DataStructures as boS

def run_BigO_analysis():
    print( "time constant function = "  )
    print(bo.checkTimeFunc1Arg_Xtimes(bo.sum2, 10, 100000))

    print("time constant function = ")
    print(bo.checkTimeFunc1Arg_Xtimes(bo.func_const, [10,3,6], 100000))

    print( "time linear function = ")
    print(bo.checkTimeFunc1Arg_Xtimes(bo.sum1, 10, 100000))

    print("time linear function = ")
    print(bo.checkTimeFunc1Arg_Xtimes(bo.func_lin, [10,3,6], 100000))

    print("time 2xlinear function = ")
    print(bo.checkTimeFunc1Arg_Xtimes(bo.func_2lin, [10,3,6], 100000))

    print("time quadratic function = ")
    print(bo.checkTimeFunc1Arg_Xtimes(bo.func_quad, [1,2,1], 100000))

    print("time combination function = ")
    print(bo.checkTimeFunc1Arg_Xtimes(bo.combinationOrder, [1, 2, 1], 100000))

    print("time match function = ")
    print(bo.checkTimeFunc2Arg_Xtimes(bo.matcher, [1, 2, 1], 3, 100000))

def run_BigO_DataStructures_analysis():
    print( "time method 1 = "  )
    print(bo.checkTimeFunc1Arg_Xtimes(boS.method1, 10000, 100))

    print( "time method 2 = "  )
    print(bo.checkTimeFunc1Arg_Xtimes(boS.method2, 10000, 100))

    print( "time method 3 = "  )
    print(bo.checkTimeFunc1Arg_Xtimes(boS.method3, 10000, 100))

    print( "time method 4 = "  )
    print(bo.checkTimeFunc1Arg_Xtimes(boS.method4, 10000, 100))

