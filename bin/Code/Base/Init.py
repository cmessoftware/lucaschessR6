import datetime
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Code
from Code import Procesador
from Code import Util, XRun
from Code.Base.Constantes import OUT_REINIT
from Code.MainWindow import LucasChessGui
from Code.Sound import Sound


def init():
    if not Code.DEBUG:
        date = datetime.datetime.now()
        log_file = f"bug-{date.strftime('%Y-%m-%d')}.log"    
        sys.stderr = Util.Log(log_file)

    main_procesador = Procesador.Procesador()
    main_procesador.set_version(Code.VERSION)
    run_sound = Sound.RunSound()
    resp = LucasChessGui.run_gui(main_procesador)
    run_sound.close()

    main_procesador.close_engines()
    main_procesador.kibitzers_manager.close()

    if resp == OUT_REINIT:
        XRun.run_lucas()
