import datetime
from Code.Config import Usuarios
from Code.QT import Colocacion
from Code.QT import Columnas
from Code.QT import Delegados
from Code.QT import Grid
from Code.QT import Iconos
from Code.QT import LCDialog
from Code.QT import QTUtil
from Code.QT import QTVarios
from Code.Util import DateSelector
from Code.QT import FormLayout
from Code.QT import QTUtil2
from Code.Services import ChessDotCom



class WChessCom(LCDialog.LCDialog):
    
    chesscom_user = ""
    date = datetime.datetime.now().strftime("%Y/%m/%d")
        
    def __init__(self, processor):
        LCDialog.LCDialog.__init__(self, processor.main_window, _("Get PNG from chess.com user"), Iconos.ChessDotCom(),
                                   "chesscomuser")
        self.configuration = processor.configuration
       
   
    def get_pgns_from_chesscom_user(self) -> str:
        while True:
            title = _("Get Pgns from Chess.com user")
            form = FormLayout.FormLayout(self, title, Iconos.ChessDotCom(), anchoMinimo=640)

            form.separador()

            form.edit(_("Chess.com user"), self.chesscom_user)
            form.separador()
            form.edit(_("Date"), self.date)

            form.separador()

            result = form.run()

            if result is None:
                return

            if not result[1]:
                QTUtil2.message_error(self, _("Chess.com user missing"))
                continue

            username = result[1][0]  
            date = datetime.datetime.strptime(result[1][1], "%Y/%m/%d")
            games = ChessDotCom.ChessDotComService.get_user_pgns(username, date)
            
            return games
    
    def cancelar(self):
        self.save_video()
        self.reject()

    def aceptar(self):
        self.grid.goto(len(self.liUsuarios) - 1, 1)
        self.grid.setFocus()
        self.save_video()
        self.chesscom_user = self.liUsuarios[0] if self.liUsuarios else None 
        self.accept()
 
    def grid_num_datos(self, grid):
        self.liUsuarios = [self.chesscom_user] if self.chesscom_user else []
        return len(self.liUsuarios)

    def grid_setvalue(self, grid, row, column, valor):
        campo = column.key
        valor = valor.strip()
        usuario = self.liUsuarios[row]
        if campo == "USUARIO":
            if valor:
                usuario.name = valor
                if usuario.number == 0:
                    self.configuration.set_player(valor)
                    self.configuration.graba()
            else:
                QTUtil.beep()

    def grid_dato(self, grid, row, o_column):
        key = o_column.key
        usuario = self.liUsuarios[row]
        if key == "DATE":
            return str(usuario.number) if usuario.number else "-"
        elif key == "USUARIO":
            return usuario.name




