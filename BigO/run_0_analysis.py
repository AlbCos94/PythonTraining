from BigO import BigO as bo

def run_all_analysis():
    print( "time constant function = "  )
    print(bo.checkTimeFunc1Arg_Xtimes(bo.sum2, 10, 100000))

    print("time constant function = ")
    print(bo.checkTimeFunc1Arg_Xtimes(bo.func_const, [10,3,6], 100000))

    print( "time linear function = ")
    print(bo.checkTimeFunc1Arg_Xtimes(bo.sum1, 10, 100000))

    print("time linear function = ")
    print(bo.checkTimeFunc1Arg_Xtimes(bo.func_lin, [10,3,6], 100000))

    print("time quadratic function = ")
    print(bo.checkTimeFunc1Arg_Xtimes(bo.func_quad, [1,2,1], 100000))