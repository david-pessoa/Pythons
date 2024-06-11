from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 # Número de trocas de tela
timer = None # Variável que conterá o id da próxima tela
checks = "✔" # Variável que conterá os "✔", representando cada tarefa concluída
# ---------------------------- RESET ------------------------------- # 
def reset_timer():
    global checks
    global reps
    checks = "✔" # Reseta a variável checks
    window.after_cancel(timer) # Cancela a próxima tela
    canvas.itemconfig(timer_text, text = "00:00") # Tempo é zerado
    label.config(text= "Timer", background= YELLOW, foreground= GREEN) # Título exibido volta a ser "Timer" na cor verde
    window.config(background= YELLOW) # Muda a cor do fundo da janela para amarelo
    canvas.config(background= YELLOW) # Muda a cor do fundo do canvas para amarelo
    check.config(background= YELLOW, text= "") # Muda a cor do fundo dos "✔" para amarelo e apaga os checks
    reps = 0 # Zera-se reps
# ---------------------------- START ------------------------------- # 
def start_timer():
    global reps
    reps += 1 # Incrementa-se reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60 # Conversão de minutos para segundos
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1: # Se reps for ímpar, então a tela exibida deve ser de "Work"
        count_down(work_sec) # Contagem regressiva
        label.config(text= "Work", foreground= YELLOW, background= GREEN) # Modificação do fundo para verde e do título para "Work", em amarelo
        window.config(background= GREEN)
        canvas.config(background= GREEN)
        check.config(background= GREEN)

    elif reps % 8 == 0: # Se reps for divisível por 8, então o usuário realizou quatro pomodoros e agora vai ter uma pausa mais longa
        global checks
        count_down(long_break_sec) # Contagem regressiva
        label.config(text= "Break", foreground= YELLOW, background= RED) # Modificação do fundo para vermelho e do título para "Break", em amarelo
        window.config(background= RED)
        canvas.config(background= RED)
        check.config(background= RED, text=checks) # Atualiza-se o número de checks
        checks += "✔" # Adiciona-se um check a variável checks

    else: # Nos casos restantes, a tela exibida deve ser a de pausa
        count_down(short_break_sec) # Contagem regressiva
        label.config(text= "Break", foreground= YELLOW, background= PINK) # Modificação do fundo para rosa e do título para "Break", em amarelo
        window.config(background= PINK)
        canvas.config(background= PINK)
        check.config(background= PINK)
        check.config(background= PINK, text=checks) # Atualiza-se o número de checks
        checks += "✔" # Adiciona-se um check a variável checks

# ---------------------------- COUNTDOWN ------------------------------- #
def count_down(count): # count é o tempo em segundos da contagem regressiva
    global timer
    min = str(count // 60) # Obtendo os minutos e segundos para exibir o tempo no formato 00:00
    sec = str(count % 60) # Transforma os números em strings

    if len(min) == 1: # Se o número dos minutos e/ou segundos possuir apenas um algarismo, é adicionado um zero à esquerda da string
        min = "0" + min
    if len(sec) == 1:
        sec = "0" + sec
    canvas.itemconfig(timer_text, text = f"{min}:{sec}") # Atualização do tempo exibido
    if count > 0:
        timer = window.after(1000, count_down, count - 1) # Enquanto o tempo não tiver chegado a zero, chama-se a função count_down() novamente após 1 segundo e o valor count - 1 é passado como parâmetro
    else: # Quando o tempo chegar a zero, a função start_timer() é chamada
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk() # Criação da janela
window.title("Pomodoro Timer") # Configuração do título da janela
window.minsize(width= 500, height= 500) # Define tamanho da janela para 500px X 500px
window.config(padx= 100, pady = 70, background= YELLOW)

label = Label(text= "Timer", font = (FONT_NAME, 40, "bold")) # Criação do título da tela, que será "Timer" no início
label.config(background= YELLOW, foreground= GREEN) # Coloca a cor do título em verde e o fundo de amarelo
label.grid(row = 0, column = 1) # Posiciona o título na "grade"

tomato_image = PhotoImage(file= "tomato.png") # Carrega a imagem do tomate
canvas = Canvas(width= 200, height= 224, background= YELLOW, highlightthickness= 0) # Cria um canvas
canvas.create_image(100, 112, image = tomato_image) # Coloca a imagem no canvas
timer_text = canvas.create_text(103, 130, text= "00:00", font= (FONT_NAME, 35, "bold"), fill= "white") # Coloca o texto que exibe o tempo no canvas
canvas.grid(row = 1, column = 1) # Posiciona o canvas na "grade"

start = Button(text= "Start", command = start_timer) # Cria o botão de Start, que ao ser pressionado chamará a função start_timer()
start.grid(row = 2, column = 0) # Posiciona o botão de start

reset = Button(text= "Reset", command = reset_timer) # Cria o botão de Reset, que ao ser pressionado chamará a função reset_timer()
reset.grid(row = 2, column = 2) # Posiciona o botão de Reset

check = Label(font = (FONT_NAME, 10, "bold"))
check.config(background= YELLOW, foreground= "#1e7216") # Cria label para exibir os "✔"
check.grid(row = 3, column = 1) # Posiciona a label

window.mainloop() # Mantém a janela aberta