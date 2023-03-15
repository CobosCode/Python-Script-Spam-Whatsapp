import pywhatkit
i = 1
while i < 10:
  pywhatkit.sendwhatmsg_instantly("+34123456789", "Texto de Prueba", 1, True, 1)
  i += 1