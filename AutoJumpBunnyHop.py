# python AutoJump/BunnyHop - by ORLY?
import keyboard as k, time as t
while True:
  if k.read_key() == "space":
    while True:
      k.press("space")
      t.sleep(0.1)
      k.release("space")
      t.sleep(0.1)
      if k.is_pressed("p"):
        k.release("space")
        break