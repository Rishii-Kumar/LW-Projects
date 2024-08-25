from txt_testing import Bunch_img_det
def check_rewards_tab():
    rewards_tab_open_checking = Bunch_img_det("E:\\Det_img\\TXT Files\\rewards_tab_Hi.txt",
                                              code_string="print('Rewards tab Hi button not found!')", img_name="Rewards tab")
    return rewards_tab_open_checking