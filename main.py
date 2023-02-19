import PySimpleGUI as sg

sg.theme("LightBrown7")

# introduction
def introduction():
  introduction = [[sg.Text("Welcome to Eggi. \nThis program is designed to help you make sense of your symptoms. \n57% of women are misdiagnosed by healthcare professionals. \nPlease enter your symptoms and we will do our best to properly diagnose you. \nThank you and we hope you feel better.")], [sg.Text("Type y for yes and n for no.")], [sg.Button("OK")]]
  window = sg.Window("Demo", introduction)
  while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
      break
  window.close()

# disorders
symovarian_cyst = [
  "pelvic pain", "painful intercourse", "painful bowel movements",
  "low fertility", "small appetite", "frequent bowel movements"
]
symmenopause = [
  "irregular periods", "vaginal dryness", "hot flashes", "chills",
  "night sweats", "sleep problems", "mood changes", "weight gain",
  "slowed metabolism", "thinning of hair", "decreasing breast size"
]
sympcos = [
  "irregular periods", "deepening of voice", "increased muscle mass",
  "balding", "excess body hair"
]
symendometriosis = [
  "abdominal pain", "back pain", "heavy bleeding",
  "bleeding during intercourse", "painful bowel movements"
]
sympolyops = [
  "heavy bleeding", "bleeding during intercourse", "white or yellow discharge",
  "spotting between period"
]

# disorders list
disorders = [
  symovarian_cyst, symmenopause, sympcos, symendometriosis, sympolyops
]

# symptoms list
symptoms = dict()
symNames = [
  "pelvic pain", "white or yellow discharge", "excess body hair",
  "painful bowel movements", "painful intercourse", "irregular periods",
  "hot flashes", "vaginal dryness", "chills", "night sweats", "sleep problems",
  "mood changes", "weight gain", "slowed metabolism", "thinning of hair",
  "dry skin", "decreasing breast size", "abdominal pain", "heavy bleeding",
  "spotting between period", "deepening of voice", "increased muscle mass",
  "balding", "bleeding during intercourse", "small appetite", "low fertility",
  "frequent bowel movements", "back pain"
]

# lists for medications
birth_control = ""
thyroid_medicine = ""
anti_depressants = ""
medications_display = ["birth control", "thyroid medicine", "anti-depressants"]
medications_code = [birth_control, thyroid_medicine, anti_depressants]

# ask age, height, first period
def ask_factors():
  factors_window = [[sg.Text("Please enter your information.")], [sg.Text("Age: ", size = (10, 1)), sg.InputText()], [sg.Text("Age when you got \nyour first period: ", size = (10, 4)), sg.InputText()], [sg.Submit()]]
  window = sg.Window("Information Window", factors_window)
  ask_factors.event, ask_factors.values = window.read()
  window.close()
  
# ask medications
def ask_medications():
  medications_window = [[sg.Text("Are you on any of the listed medications? Type y for yes and n for no.")], [sg.Text("Birth Control: ", size = (15, 1)), sg.InputText()], [sg.Text("Thyroid Medicine: ", size = (15, 1)), sg.InputText()], [sg.Text("Anti-Depressants: ", size = (15, 1)), sg.InputText()], [sg.Submit()]]
  window = sg.Window("Medications Window", medications_window)
  ask_medications.event, ask_medications.values = window.read()
  window.close()

# ask common symptoms
def ask_symptoms():
  symptoms_window = [[sg.Text("Which of the following symptoms are you experiencing in the past 60 days?")], [sg.Button("CONTINUE")]]
  window = sg.Window("Symptoms Window", symptoms_window)
  event, values = window.read()
  window.close()

  for sym in symNames:
    symptom_window = [[sg.Text({sym})], [sg.Button("YES")], [sg.Button("NO")]]
    window = sg.Window("Symptom", symptom_window)
    while True:
      ask_symptoms.event, ask_symptoms.values = window.read()
      if ask_symptoms.event == "YES":
        symptoms[sym] = 1
        break
        window.close()
      else: 
        symptoms[sym] = 0
        break
        window.close()
      window.close()
    window.close()

# check menopause
def check_menopause():
  if int(ask_factors.values[0]) >= 45 and int(ask_factors.values[0]) <= 69:
    s = 0
    for sym in symmenopause:
      s += symptoms[sym]

    if len(symmenopause) / 2 <= s:
      menopause_window = [[sg.Text("You may be going through menopause. \nMenopause is a natural decline in the reproductive hormones that occur during your \n40s to 50s, which causes for your period to not occur anymore.")], [sg.Button("OK")]]
      window = sg.Window("Menopause", menopause_window)
      while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
          break
      window.close()
    else:
      menopause_2_window = [[sg.Text("You may experience menopause soon because you are \nin the age range for it.")], [sg.Button("OK")]]
      window = sg.Window("Menopause", menopause_2_window)
      while True:
        event, values = window.read()
        if event == "OK" or event == sg.WIN_CLOSED:
          break
      window.close()

# check first period range irregularities
def check_first_period_irregularities():
  if (int(ask_factors.values[0]) - int(ask_factors.values[1])) <= 2:
    irregularities_window = [[sg.Text("You may have some symptoms because your period is not regular yet.")], [sg.Button("OK")]]
    window = sg.Window("First Period Irregularities", irregularities_window)
    while True:
      event, values = window.read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()

# check medications
def check_medications():

  if ask_medications.values[0] == "y":
    medications_window = [[sg.Text("You may be experiencing some symptoms because you are on birth control")], [sg.Button("OK")]]
    window = sg.Window("Birth Control", medications_window)
    while True:
      event, values = window.Read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()
    
  if ask_medications.values[1] == "y":
    medications_window = [[sg.Text("You may be experiencing some symptoms because you are on thyroid medicine")], [sg.Button("OK")]]
    window = sg.Window("Thyroid Medicine", medications_window)
    while True:
      event, values = window.Read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()
    
  if ask_medications.values[2] == "y":
    medications_window = [[sg.Text("You may be experiencing some symptoms because you are on anti-depressants")], [sg.Button("OK")]]
    window = sg.Window("Anti-Depressants", medications_window)
    while True:
      event, values = window.Read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()

# check ovarian cyst
def check_ovarian_cyst():
  s = 0
  for sym in symovarian_cyst:
    s += symptoms[sym]
  if len(symovarian_cyst) / 2 <= s:
    ovarian_cyst_window = [[sg.Text("You may be at risk for ovarian cysts. \nAn ovarian cyst is a cyst, which is a solid or fluid-filled sac/pocket, \non or within the surface of an ovary. \nFor a further diagnosis, \nask your doctor for a pelvic exam or a transvaginal ultrasound.")], [sg.Button("OK")]]
    window = sg.Window("Ovarian Cyst", ovarian_cyst_window)
    while True:
      event, values = window.read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()
  else:
    ovarian_cyst_window_2 = [[sg.Text("Yay! Your symptoms show that you are not at risk for ovarian cysts.")], [sg.Button("OK")]]
    window = sg.Window("Ovarian Cyst", ovarian_cyst_window_2)
    while True:
      event, values = window.read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()

# check pcos
def check_pcos():
  s = 0
  for sym in sympcos:
    s += symptoms[sym]
  if len(sympcos) / 2 <= s:
    pcos_window = [[sg.Text("You may be at risk for Polycystic Ovary Syndrome (PCOS). \nPCOS is a hormonal disorder that leads to the ovaries becoming \nenlarged and small cysts forming on the outer edges. \nFor a further diagnosis, ask your doctor for a \npelvic exam, blood tests, and an ultrasound.")], [sg.Button("OK")]]
    window = sg.Window("PCOS", pcos_window)
    while True:
      event, values = window.read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()
  else:
    pcos_window_2 = [[sg.Text("Yay! Your symptoms show that you are not at risk for \nPolycystic Ovary Syndrome (PCOS).")], [sg.Button("OK")]]
    window = sg.Window("PCOS", pcos_window_2)
    while True:
      event, values = window.read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()
    
# check endometriosis
def check_endometriosis():
  s = 0
  for sym in symendometriosis:
    s += symptoms[sym]
  if len(symendometriosis) / 2 <= s:
    endometriosis_window = [[sg.Text("You may be at risk for endometriosis. \nThis is when the uterine lining that sheds every month \nis growing on the outside of the uterus. \nFor a further diagnosis, \nask your doctor for a CA125 test.")], [sg.Button("OK")]]
    window = sg.Window("Endometriosis", endometriosis_window)
    while True:
      event, values = window.read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()
  else:
    endometriosis_window_2 = [[sg.Text("Yay! Your symptoms show that you are not at risk for endometriosis.")], [sg.Button("OK")]]
    window = sg.Window("Endometriosis", endometriosis_window_2)
    while True:
      event, values = window.read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()

# check polyps
def check_polyps():
  s = 0
  for sym in sympolyops:
    s += symptoms[sym]
  if len(sympolyops) / 2 <= s:
    polyps_window = [[sg.Text("You may be at risk for polyps. \nPolyps are fingerlike tissue growths on the cervix. \nFor a further diagnosis, \nwe recommend you get a pelvic exam and a pap smear.")], [sg.Button("OK")]]
    window = sg.Window("Polyps", polyps_window)
    while True:
      event, values = window.read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()
  else:
    polyps_window_2 = [[sg.Text("Yay! Your symptoms show that you are not at risk for polyops.")], [sg.Button("OK")]]
    window = sg.Window("Polyps", polyps_window_2)
    while True:
      event, vales = window.read()
      if event == "OK" or event == sg.WIN_CLOSED:
        break
    window.close()

# final
def final():
  final_window = [[sg.Text("Thank you for using Eggi! \nWe hope that you have guidance on your next steps now!")], [sg.Button("FINISH")]]
  window = sg.Window("End", final_window)
  while True:
    event, values = window.read()
    if event == "FINISH" or event == sg.WIN_CLOSED:
      break
  window.close()
    
def run_everything():
  introduction()
  ask_factors()
  ask_medications()
  ask_symptoms()
  check_menopause()
  check_first_period_irregularities()
  check_medications()
  check_ovarian_cyst()
  check_pcos()
  check_endometriosis()
  check_polyps()
  final()

run_everything()