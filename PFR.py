from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import Image
import webbrowser
import random


mainwindow = Tk()
mainwindow.title("Virtual Lab")

# wb = load_workbook(filename='data.xlsx')

file = "Webp.net-gifmaker (1).gif"
info = Image.open(file)
frames = info.n_frames
im = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]
count = 0
anim = None


canvas = Canvas(mainwindow)
canvas.pack(expand=True)

cont = ttk.Frame(mainwindow)
cont.pack()


homebutton = Button(
    mainwindow,
    text="HOME",
    font="Times 12 bold",
    command=lambda: {
        cont.forget(),
        introcanvas.forget(),
        theorycanvas.forget(),
        samplecalcanvas.forget(),
        canvas.pack(),
        simulationcanvas.forget(),
    },
    width=20,
)
homebutton.pack(side=BOTTOM, padx=(10, 10), pady=(10, 10))

introcanvas = Canvas(
    mainwindow,
    highlightthickness=1,
    highlightbackground="black",
)
theorycanvas = Canvas(mainwindow, highlightthickness=1, highlightbackground="black")
samplecalcanvas = Canvas(mainwindow, highlightthickness=1, highlightbackground="black")
simulationcanvas = Canvas(mainwindow, highlightthickness=1, highlightbackground="black")

intervals = [5, 10, 15]
interval = StringVar()
interval.set(intervals[0])

photo = PhotoImage(file="img.png")
photo1 = PhotoImage(file="water.png")
photo2 = PhotoImage(file="withoutwater.png")
photo3 = PhotoImage(file="intro.png")
photo4 = PhotoImage(file="theory.png")
photo5 = PhotoImage(file="sample calc.png")
lblphoto = Label(canvas, image=photo)
lblphoto.grid(row=2, column=4, rowspan=6, columnspan=8, padx=(5, 0), pady=(10, 0))

namelabel = Label(
    canvas,
    text="        Shreyansh Bindage"
    "                           Swapnil Srivastava                        "
    "   Nikhil Shinde"
    + "\n"
    + "shreyansh.bindage18@vit.edu         swapnil.srivastava18@vit.edu          "
    "nikhil.shinde18@vit.edu"
    + "\n"
    + "\n"
    + "Rashad Ahmad                        Vedant Raut"
    + "\n"
    + "rashad.ahmad18@vit.edu             vedant.raut18@vit.edu",
    justify=CENTER,
    font="Times 14 bold",
    pady=10,
)
namelabel.grid(row=8, column=2, columnspan=12, padx=(35, 35), pady=(10, 0))

aimlabel = Label(
    canvas,
    text="Study of Residence Time Distribution in a PFR",
    justify=LEFT,
    font="Times 18 bold",
    pady=10,
)
aimlabel.grid(row=1, column=2, columnspan=10, padx=(35, 35), pady=(10, 0))


def intro():
    introcanvas.pack()
    aimlabel1 = Label(
        introcanvas,
        text="Study of Residence Time Distribution in a PFR",
        justify=LEFT,
        font="Times 18 bold",
        pady=10,
    )
    aimlabel1.grid(row=1, column=2, columnspan=10, padx=(35, 35), pady=(10, 0))
    introphoto = Label(introcanvas, image=photo3)
    introphoto.grid(
        row=2, column=2, rowspan=6, columnspan=10, padx=(35, 35), pady=(10, 10)
    )


def theory():
    theorycanvas.pack()
    aimlabel2 = Label(
        theorycanvas,
        text="Study of Residence Time Distribution in a PFR",
        justify=LEFT,
        font="Times 18 bold",
        pady=10,
    )
    aimlabel2.grid(row=1, column=2, columnspan=10, padx=(35, 35), pady=(10, 0))
    theoryphoto = Label(theorycanvas, image=photo4)
    theoryphoto.grid(
        row=2, column=2, rowspan=6, columnspan=10, padx=(35, 35), pady=(10, 10)
    )


z = 0
values = []
label = Label(
    simulationcanvas,
    text="Time Elapsed 00 seconds     Conductivity Meter Reading 000.0000",
    justify=LEFT,
    font="Times 14 bold",
    pady=10,
)
label.grid(row=3, column=7, padx=(40, 10))


def simulation():
    def animation(count):
        global anim

        im2 = im[count]
        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = simulationcanvas.after(14500, lambda: animation(count))

    gif_label = Label(simulationcanvas, image="")
    gif_label.grid(row=4, column=7, rowspan=4, columnspan=2, padx=(40, 10))
    values = []

    for t in range(0, 400, 1):
        y = (
            (
                ((t / 213.88714) ** 61)
                * ((62 ** 62) / np.math.factorial(61))
                * np.exp((-t * 62) / 213.88714)
                * (1 / 213.88714)
            )
            * 29056.60781
            + 780
            + random.random()
        )
        values.append(y)

    def calculate(label):
        def animate():
            try:
                global z
                i = interval.get()
                z += 1
                label.configure(
                    text="Time Elapsed "
                    + str(z)
                    + " seconds     Conductivity Meter Reading "
                    + str(round(values[z], 4))
                )
                if z % int(i) == 0:
                    dataTV.insert("", "end", text=z, values=(values[z]))
                label.after(700, animate)
            except IndexError:
                w = Toplevel()
                w.title("Simulation Completed!!")
                w.geometry("400x140")
                name = Label(
                    w,
                    text="Simulation Successfully Completed\nData is ready to be exported",
                    font="Times 16 bold",
                )
                name.grid(row=0, column=0, padx=(20, 10), pady=(20, 20))
                start.grid(
                    row=7,
                    column=2,
                    columnspan=5,
                    padx=(10, 10),
                    pady=(10, 10),
                    sticky=E,
                )
                simulationcanvas.after_cancel(anim)

        animate()

    simulationcanvas.pack()
    aimlabel3 = Label(
        simulationcanvas,
        text="Study of Residence Time Distribution in a PFR",
        justify=LEFT,
        font="Times 18 bold",
        pady=10,
    )
    aimlabel3.grid(row=2, column=2, columnspan=5, padx=(10, 10), pady=(10, 40))
    equipspectitle = Label(
        simulationcanvas,
        text="Equipment Specifications",
        justify=LEFT,
        font="Times 18 bold",
        pady=10,
    )
    equipspectitle.grid(row=3, column=2, padx=(10, 10), sticky=W)
    equipspec = Label(
        simulationcanvas,
        text="Length of Reactor  : 182 cm \nInner Diameter       : 2 in \nOuter Diameter      : 2.25 in \nFlowrate                : 24.8 mL/s \nVolume of Reactor: 3.7 L\nConductivity probe calibrated using a standard NaCl solution of 500mg",
        font="Times 14",
        justify=LEFT,
        pady=10,
    )
    equipspec.grid(row=4, column=2, columnspan=5, padx=(10, 10), sticky=W)
    showsetup = Button(
        simulationcanvas,
        text="Show Set-Up",
        font="Times 12 bold",
        command=lambda: {
            gif_label.config(image=photo2),
            startflow.grid(row=6, column=2, columnspan=5, padx=(10, 10), pady=(10, 10)),
        },
        width=13,
    )
    showsetup.grid(
        row=6, column=2, columnspan=5, padx=(10, 10), pady=(10, 10), sticky=W
    )
    startflow = Button(
        simulationcanvas,
        text="Start Flow",
        font="Times 12 bold",
        command=lambda: {
            gif_label.config(image=photo1),
            injecttracer.grid(
                row=6, column=2, columnspan=5, padx=(10, 10), pady=(10, 10), sticky=E
            ),
        },
        width=13,
    )
    injecttracer = Button(
        simulationcanvas,
        text="Inject Tracer",
        font="Times 12 bold",
        command=lambda: {calculate(label), animation(count)},
        width=13,
    )
    start = Button(
        simulationcanvas,
        text="Export data",
        font="Times 12 bold",
        command=lambda: {},
        width=13,
    )

    timeinterval = Label(
        simulationcanvas,
        text="Select time interval for recording readings (in sec)",
        justify=LEFT,
        font="Times 12 bold",
        pady=10,
    )
    timeinterval.grid(
        row=7, column=2, columnspan=2, padx=(10, 10), pady=(10, 10), sticky=W
    )
    timeintervalDropDown = OptionMenu(simulationcanvas, interval, *intervals)
    timeintervalDropDown.grid(row=7, column=3, padx=(10, 10), pady=(10, 10))

    dataTV = ttk.Treeview(
        master=simulationcanvas, height=10, columns=("File Name", "Guardian det")
    )
    dataTV.grid(row=9, column=2, columnspan=4, sticky=W, padx=(10, 10), pady=(10, 10))
    style = ttk.Style(simulationcanvas)
    style.configure("Treeview", rowheight=18)
    vsb = ttk.Scrollbar(
        master=simulationcanvas, orient="vertical", command=dataTV.yview
    )
    vsb.grid(sticky="NS", row=9, column=3, pady=(10, 10))
    dataTV.configure(yscrollcommand=vsb.set)
    dataTV.column("#0", width=120)
    dataTV.column("#1", width=240)
    dataTV.heading("#0", text="Time")
    dataTV.heading("#1", text="Conductivity Meter Reading")
    dataTV["displaycolumns"] = "0"


"""
def export():
    fname = StringVar()
    floc = StringVar()
    t = Toplevel()
    t.title("Export Data")
    name = Label(t, text="File Name")
    name.grid(row=0, column=0, padx=(20, 10), pady=(20, 20))
    namee = Entry(t, textvariable=fname)
    namee.grid(row=0, column=1, padx=(10, 20), pady=(20, 20))
    loc = Label(t, text="File Path")
    loc.grid(row=1, column=0, padx=(20, 10), pady=(20, 20))
    loce = Entry(t, textvariable=floc)
    loce.grid(row=1, column=1, padx=(10, 20), pady=(20, 20))
    ws = wb['Design']
    i = interval.get()
    for g in range (0, 400, int(i)):
        ws['B'+str(g)] = values[g]


    def adata():
        wb.save(str(floc.get()) + "/" + str(fname.get()) + ".xlsx")

    ok = Button(t, text="OK", command=lambda: [t.destroy(), adata()])
    ok.grid(row=3, column=0, padx=(20, 20), pady=(10, 10), columnspan=2)
"""


def samplecal():
    samplecalcanvas.pack()
    aimlabel4 = Label(
        samplecalcanvas,
        text="Study of Residence Time Distribution in a PFR",
        justify=LEFT,
        font="Times 18 bold",
        pady=10,
    )
    aimlabel4.grid(row=1, column=2, columnspan=10, padx=(35, 35), pady=(10, 0))
    samplecalphoto = Label(samplecalcanvas, image=photo5)
    samplecalphoto.grid(
        row=2, column=2, rowspan=6, columnspan=10, padx=(35, 35), pady=(10, 10)
    )


button1 = Button(
    canvas,
    text="Introduction",
    font="Times 12 bold",
    command=lambda: {canvas.forget(), intro()},
    width=20,
)
button1.grid(row=2, column=2, rowspan=2, padx=(50, 50), pady=(30, 30))

button2 = Button(
    canvas,
    text="Theory",
    font="Times 12 bold",
    command=lambda: {canvas.forget(), theory()},
    width=20,
)
button2.grid(row=3, column=2, rowspan=2, padx=(50, 50), pady=(30, 30))

button3 = Button(
    canvas,
    text="Simulation",
    font="Times 12 bold",
    command=lambda: {canvas.forget(), simulation()},
    width=20,
)
button3.grid(row=4, column=2, rowspan=2, padx=(50, 50), pady=(30, 30))

button4 = Button(
    canvas,
    text="Write-Up",
    font="Times 12 bold",
    command=lambda: {
        webbrowser.open_new(
            "https://drive.google.com/file/d/1RYObsrb6eS4lUptp9HyXdMrN3a4LD8RH/view?usp=sharing"
        )
    },
    width=20,
)
button4.grid(row=5, column=2, rowspan=2, padx=(50, 50), pady=(30, 30))

button5 = Button(
    canvas,
    text="Sample Calculations",
    font="Times 12 bold",
    command=lambda: {canvas.forget(), samplecal()},
    width=20,
)
button5.grid(row=6, column=2, rowspan=2, padx=(50, 50), pady=(30, 30))

mainwindow.mainloop()
