import math
summ_pnt_list = []

def main():
    for i in range (9):
        print('##################################################################################')
        print("For Package " + str(i+1))

        c = raw_input('1. Is the 2D Camera able to identify Package  ' + str(i+1) + ' ? (y/n) ->')
        if(c == 'y'):
            c_pnt = 50
        else:
            c_pnt = 0
        ##################################################################################
        o_r = raw_input('2. Are you able to view and update the Incoming Orders status for Package ' +  str(i+1)  + ' ? (y/n) ->')
        if(o_r == 'y'):
            o_r_pnt = 20
        else:
            o_r_pnt = 0
        ##################################################################################
        ur5_1 = raw_input('3. Is your UR5#1 able to pick the Package ' + str(i+1) + ' from the shelf and place it on the conveyor? (y/n) -> ')
        if(ur5_1 == 'y'):
            ur5_1_pnt = 100
        else:
            ur5_1_pnt = 0
        #################################################################################
        ur5_2 = raw_input('4. Is your UR5#2 able to pick the Package ' + str(i+1) + ' from the conveyor belt and segregate it into colour corresponding bins?(y/n) -> ')
        if(ur5_2 == 'y'):
            ur5_2_pnt = 100
        else:
            ur5_2_pnt = 0
        #################################################################################
        ur5_s = raw_input('5. Are you able to update the status of Package ' + str(i+1) + ' in the Orders Dispatch and Orders Shipped Spreadsheets? (y/n) -> ')
        if(ur5_s == 'y'):
            ur5_s_pnt = 40
        else:
            ur5_s_pnt = 0   
        #################################################################################
        ur5_e = raw_input('6. Are you able to send Dispatch and Shipped status of Package ' + str(i+1) + ' emails to the customer? (y/n) ->')
        if(ur5_e == 'y'):
            ur5_e_pnt = 40
        else:
            ur5_e_pnt = 0   
        ################################################################################
        summ = c_pnt + o_r_pnt + ur5_1_pnt + ur5_2_pnt + ur5_s_pnt + ur5_e_pnt
        ################################################################################
        pkg_coll = raw_input('7. Total Number of collisions for Package ' + str(i+1) + ' ? (0 or +ve integer) ->')
        pkg_coll_pnt = int(pkg_coll) * 20     
        ################################################################################
        sim_time = raw_input('8. What is your simulation time for Package ' + str(i+1) + ' (+ve integer) -> ')
        sim_pnt = ( int(sim_time) )
        dt = int(200 * (float(500 - sim_pnt) / 500))
        wop = raw_input('9. What is the type of Package ' + str(i+1) + ':  HP, MP, LP -> ')
        if (wop == 'HP'):
            wop_pnt = 4
        elif(wop == 'MP'):
            wop_pnt = 2
        elif(wop == 'LP'):
            wop_pnt = 1
        summ_pnt = (int(wop_pnt) * ((dt - pkg_coll_pnt) + (summ)))
        ################################################################################
        summ_pnt_list.append(summ_pnt)
    #####################################################################################
    Summation_pkg_handling = sum(summ_pnt_list)
    #####################################################################################
    print('##################################################################################')
    dash = raw_input('Are you able to build a dynamic dashboard interface to show the inventory processes (y/n) ->')
    if(dash == 'y'):
        dash_pnt = 50
    else:
        dash_pnt = 0
    #####################################################################################
    print('##################################################################################')
    no_coll = raw_input('Total number of UR5 collisions with other models? (0 or +ve integer) -> ')
    no_coll_pnt = int(no_coll) * (20)
    #####################################################################################
    Summation_general = dash_pnt - no_coll_pnt

    Total_Score = Summation_pkg_handling + Summation_general
    if(Total_Score < 0):
        Total_Score = 0

    print('##################################################################################')
    Final_Score = (float(Total_Score) / 11600 ) * 100
    #####################################################################################
    print("\n\n Task-5 Self-Eval Score: {}".format(str(Final_Score)) )
    

if __name__ == '__main__':
	main()

