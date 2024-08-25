from Det_img import Bunch_img_det
# frequent image detections
def det_new_tab(clk=0):
    new_tab = Bunch_img_det("E:\\Det_img\\TXT Files\\New_tab.txt", code_string="pass", kt=clk)
    return new_tab

def det_rewards_tab(clk=0):
    rewards_tab = Bunch_img_det("E:\\Det_img\\TXT Files\\Rewards_tab.txt", code_string="pass", kt=clk)
    return rewards_tab

def det_etab():
    etab = Bunch_img_det("E:\\Det_img\\TXT Files\\Edge_tab.txt", code_string="pass", kt=0)
    return etab


# repeating image detections
def find_searchbar():
    clk_on_srch_bar = Bunch_img_det("E:\\Det_img\\TXT Files\\Searchbar.txt", code_string="pass")
    return clk_on_srch_bar


def det_and_visuals():
    # Check for various visual cues indicating Android visuals are not found
    check_visual = Bunch_img_det("E:\\Det_img\\TXT Files\\Android_visuals.txt",
                                 code_string="print('Android Visuals not found!')", kt=0, img_name=0)
    return check_visual


def det_searched():
    check_searched = Bunch_img_det("E:\\Det_img\\TXT Files\\Android_searched.txt",
                                   code_string="pass", kt=0, img_name="Android searched")
    return check_searched