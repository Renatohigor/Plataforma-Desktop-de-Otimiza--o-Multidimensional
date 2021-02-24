from Model.M_prob.CologneClass01 import Colony_01
from Model.M_prob.CologneClass01_1 import Colony_01_1
from Model.M_prob.CologneClass03 import Colony_03
from Model.M_prob.CologneClass03_1 import Colony_03_1

from Model.M_prob.pso_0_1 import Swarm_1
from Model.M_prob.pso_1_0 import Swarm_2
from Model.M_prob.pso_1_1 import Swarm_3
from Model.M_prob.GA import GA


def metodoPROB(ID,parametros):
    if ID == 0:
        acv = Colony_01()

        return  acv.main(f=parametros[0],
                         dim=parametros[1],
                         n=parametros[2],
                         beta0=parametros[3],
                         alpha=parametros[4],
                         numGer=parametros[5],
                         paraAbsorcao=parametros[6],
                         tetha=parametros[7],
                         )

    if ID == 1:
        acv = Colony_01_1()

        return acv.main(f=parametros[0],
                        dim=parametros[1],
                        n=parametros[2],
                        beta0=parametros[3],
                        alpha=parametros[4],
                        numGer=parametros[5],
                        paraAbsorcao=parametros[6],
                        tetha=parametros[7],
                        )

    if ID == 2:
        acv = Colony_03()

        return  acv.main(f=parametros[0],
                         dim=parametros[1],
                         n=parametros[2],
                         beta0=parametros[3],
                         beta_min=parametros[4],
                         alpha=parametros[5],
                         numGer=parametros[6],
                         paraAbsorcao=parametros[7],
                         tetha=parametros[8],
                         )

    if ID == 3:
        acv = Colony_03_1()

        return acv.main(f=parametros[0],
                        dim=parametros[1],
                        n=parametros[2],
                        beta0=parametros[3],
                        beta_min=parametros[4],
                        alpha=parametros[5],
                        numGer=parametros[6],
                        paraAbsorcao=parametros[8],
                        tetha=parametros[9],
                        )

    if ID == 4:
        pso = Swarm_1(n=parametros[0])

        return  pso.PSO(f=parametros[1],
                        domain=parametros[2],
                        itr=parametros[3],
                        initial_velocity=parametros[4]
                        )


    if ID == 5:
        pso = Swarm_2(n=parametros[0])
        return pso.PSO(f=parametros[1],
                       domain=parametros[2],
                       itr=parametros[3],
                       initial_velocity=parametros[4],
                       w=parametros[5],
                       c1=parametros[6],
                       c2=parametros[7])


    if ID == 6:
        pso = Swarm_3(n=parametros[0])

        return pso.PSO(f=parametros[1],
                       domain=parametros[2],
                       itr=parametros[3],
                       initial_velocity=parametros[4],
                       w_ini=parametros[5],
                       w_fin=parametros[6],
                       c1_ini=parametros[7],
                       c1_fin=parametros[8],
                       c2_ini=parametros[9],
                       c2_fin=parametros[10]
                       )

    if ID == 7:
        fitness_list, bits_values, real_values, func_value =GA(parametros[1:]).solve(parametros[0])
        print(fitness_list)
        return fitness_list, bits_values, real_values, func_value