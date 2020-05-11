import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json

datos={}	

def main(args):
  juegos=("Ahorcado","TaTeTi","Otello","Salir")
  jugadas=[]
  sigo_jugando=True
  nom=""
  while sigo_jugando:
    layout=[[sg.Text('Jugador')],[sg.InputText(key='nom')],[sg.Listbox(values=(juegos),key='juegos',size=(40,10))],[sg.Button('Elije')]]
    window = sg.Window('Jugadas').Layout(layout)
    event, values=window.Read()
    if nom == "":
      nom=values["nom"]
    else:         
      window.FindElement('nom').update(nom)	
    #print(f"Evento:{event}")  
    if event == 'Elije':
      juego=values["juegos"][0]
      if juego == 'Ahorcado':
        hangman.main()
        jugadas.append('Ahorcado')
      elif juego == "TaTeTi":
        tictactoeModificado.main()
        jugadas.append('TaTeTi')
      elif juego == "Otello":
        reversegam.main()
        jugadas.append('Otello')
      elif juego == "Salir":
        sigo_jugando=False		
        datos.setdefault(nom,jugadas)
        print(datos)
        with open("jugadas.json",'a') as file:
          json.dump(datos,file,indent=2)
          file.close() 
          break
  window.Close()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
