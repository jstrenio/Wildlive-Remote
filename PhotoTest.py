#tests for remote camera

#activate listen with text 'photo'
def send_text():
    txtFile = 'sms_input.txt'
    txt = 'Photo'

    with open(txtFile) as f:
        f.write(txt)
    f.close()

send_text()
