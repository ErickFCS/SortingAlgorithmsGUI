import pygame as pg
from random import shuffle, randint
from time import sleep
from sys import argv


class Configuration:
    screen_Size = (1366, 768)
    background1 = "#C38774"
    background2 = "#563440"
    foreground1 = "#2274A5"
    foreground2 = "#FFFFFF"
    barWidth = 7
    sleepTime = 2
    arrRange = (1, 101)

    def __init__(self) -> None:
        pass

    def setScreenSize(width=0, height=0):
        Configuration.screen_Size = (width, height)

    def setArrLen(start, end):
        Configuration.arrRange = (start, end + 1)

    def setDefault():
        Configuration.screen_Size = (0, 0)
        Configuration.background1 = "#C4B1AB"
        Configuration.background2 = "#563440"
        Configuration.foreground1 = "#2274A5"
        Configuration.foreground2 = "#FFFFFF"
        Configuration.barWidth = 5
        Configuration.sleepTime = 100
        Configuration.arrRange = (1, 101)


class Baritas:
    def __init__(self, width=20, height=20, xpos=0, ypos=0, anchor="center"):
        self.rect = pg.Rect(0, 0, width, height)
        self.place(xpos, ypos, anchor)

    def place(self, xpos, ypos, anchor):
        ok = 0
        if anchor in ["topleft", "tl", "nw"]:
            self.rect.topleft = (xpos, ypos)
            ok = 1
        elif anchor in ["top", "t", "n"]:
            self.rect.top = (xpos, ypos)
            ok = 1
        elif anchor in ["topright", "tr", "ne"]:
            self.rect.topright = (xpos, ypos)
            ok = 1
        elif anchor in ["left", "l", "w"]:
            self.rect.left = (xpos, ypos)
            ok = 1
        elif anchor in ["center", "middle", "c", "m"]:
            self.rect.center = (xpos, ypos)
            ok = 1
        elif anchor in ["right", "r", "e"]:
            self.rect.right = (xpos, ypos)
            ok = 1
        elif anchor in ["bottomleft", "bl", "sw"]:
            self.rect.bottomleft = (xpos, ypos)
            ok = 1
        elif anchor in ["bottom", "b", "s"]:
            self.rect.bottomleft = (xpos, ypos)
            ok = 1
        elif anchor in ["bottomright", "br", "se"]:
            self.rect.bottomright = (xpos, ypos)
            ok = 1
        if ok == 1:
            self.xpos = xpos
            self.ypos = ypos
            self.anchor = anchor

    def move(self, x, y):
        self.place(self.xpos + x, self.ypos + y, self.anchor)


class Pantallaball:
    def __init__(self) -> None:
        pg.init()

    def start(self):
        self.screenSize = pg.display.get_desktop_sizes()[0]
        self.window = pg.display.set_mode((0, 0), pg.RESIZABLE)
        self.clock = pg.time.Clock()
        pg.display.set_caption("Sorting Algoritms")
        self.Arial = pg.font.match_font("Arial")
        self.titles = pg.font.Font(self.Arial, 32)
        self.description = pg.font.Font(self.Arial, 20)

    def checkEventsMenu(self):

        def isBetween(val, vals):
            return (val >= vals[0] and val <= vals[1])

        def bSClick():
            arr = list(
                range(Configuration.arrRange[0], Configuration.arrRange[1]))
            shuffle(arr)
            self.bubbleSort(arr)
            self.menu()
            self.update()

        def sSClick():
            arr = list(
                range(Configuration.arrRange[0], Configuration.arrRange[1]))
            shuffle(arr)
            self.selectionSort(arr)
            self.menu()
            self.update()

        def iSClick():
            arr = list(
                range(Configuration.arrRange[0], Configuration.arrRange[1]))
            shuffle(arr)
            self.insertionSort(arr)
            self.menu()
            self.update()

        def mSClick():
            arr = list(
                range(Configuration.arrRange[0], Configuration.arrRange[1]))
            shuffle(arr)
            self.mergeSort(arr, arr)
            self.isOrdered(arr)
            self.menu()
            self.update()

        def qSClick():
            arr = list(
                range(Configuration.arrRange[0], Configuration.arrRange[1]))
            shuffle(arr)
            self.quickSort(arr, 0, len(arr))
            self.isOrdered(arr)
            self.menu()
            self.update()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    return 0
                if event.type == pg.MOUSEBUTTONDOWN:
                    xpos, ypos = pg.mouse.get_pos()
                    if isBetween(xpos, [87, 87 + 340]) and isBetween(ypos, [56, 56 + 300]):
                        bSClick()
                    if isBetween(xpos, [513, 513 + 340]) and isBetween(ypos, [56, 56 + 300]):
                        sSClick()
                    if isBetween(xpos, [940, 940 + 340]) and isBetween(ypos, [56, 56 + 300]):
                        iSClick()
                    if isBetween(xpos, [300, 300 + 340]) and isBetween(ypos, [414, 414 + 300]):
                        mSClick()
                    if isBetween(xpos, [727, 727 + 340]) and isBetween(ypos, [414, 414 + 300]):
                        qSClick()
            self.clock.tick(30)

    def update(self):
        pg.display.update()

    def sorting(self, arr, index1, index2):

        def drawArr(arr, index1, index2):
            width = Configuration.barWidth
            self.window.fill(Configuration.background1)
            for i, v in enumerate(arr):
                if i == index1:
                    pg.draw.rect(self.window, "#DD0000", Baritas(
                        width, v * width, (Configuration.screen_Size[0] - (Configuration.arrRange[1] - 1) * Configuration.barWidth) / 2 + i * Configuration.barWidth, Configuration.screen_Size[1] - (Configuration.screen_Size[1] - (Configuration.arrRange[1] - 1) * Configuration.barWidth) / 2, "bottomleft"))
                elif i == index2:
                    pg.draw.rect(self.window, "#00DD00", Baritas(
                        width, v * width, (Configuration.screen_Size[0] - (Configuration.arrRange[1] - 1) * Configuration.barWidth) / 2 + i * Configuration.barWidth, Configuration.screen_Size[1] - (Configuration.screen_Size[1] - (Configuration.arrRange[1] - 1) * Configuration.barWidth) / 2, "bottomleft"))
                else:
                    pg.draw.rect(self.window, "#0000DD", Baritas(
                        width, v * width, (Configuration.screen_Size[0] - (Configuration.arrRange[1] - 1) * Configuration.barWidth) / 2 + i * Configuration.barWidth, Configuration.screen_Size[1] - (Configuration.screen_Size[1] - (Configuration.arrRange[1] - 1) * Configuration.barWidth) / 2, "bottomleft"))
            self.update()

        drawArr(arr, index1, index2)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        sleep(Configuration.sleepTime / 1000)

    def menu(self):
        self.window.fill(Configuration.background1)

        def drawRect(xpos, ypos):
            pg.draw.rect(self.window, Configuration.background2,
                         Baritas(340, 300 - 80, xpos, ypos + 40, "topleft"))
            pg.draw.rect(self.window, Configuration.background2,
                         Baritas(340 - 80, 300, xpos + 40, ypos, "topleft"))
            pg.draw.circle(self.window, Configuration.background2,
                           (xpos + 40, ypos + 40), 40)
            pg.draw.circle(self.window, Configuration.background2,
                           (xpos + 300, ypos + 40), 40)
            pg.draw.circle(self.window, Configuration.background2,
                           (xpos + 40, 300 - 40 + ypos), 40)
            pg.draw.circle(self.window, Configuration.background2,
                           (xpos + 300, 300 - 40 + ypos), 40)

        def drawTitle(text, xpos, ypos):
            title = self.titles.render(text, True, Configuration.foreground1)
            titleRect = title.get_rect()
            titleRect.center = (xpos, ypos)
            self.window.blit(title, titleRect)

        def drawDescription(text, xpos, ypos):
            splited = text.split("-")
            for i, v in enumerate(splited):
                text = self.description.render(
                    v, True, Configuration.foreground2)
                textRect = text.get_rect()
                textRect.center = (xpos, ypos + i * 20)
                self.window.blit(text, textRect)

        drawRect(87, 56)
        drawRect(513, 56)
        drawRect(940, 56)
        drawRect(300, 414)
        drawRect(727, 414)

        drawTitle("Bubble Sort", 257, 206 - 110)
        drawTitle("Selection Sort", 679, 206 - 110)
        drawTitle("Insertion Sort", 1110, 206 - 110)
        drawTitle("Merge Sort", 470, 564 - 110)
        drawTitle("Quick Sort", 897, 564 - 110)

        drawDescription("Bubble Sort compara-y ordena elementos adyacentes de-una lista intercambiándolos si-están en el orden incorrecto,-repitiendo este proceso hasta-que la lista esté ordenada.-Es simple pero ineficiente para-listas grandes.", 257, 56 + (300 - 20*7 + 43)/2)
        drawDescription("Selection Sort selecciona repetidamente-el elemento más pequeño y lo coloca-en su posición correcta en la lista,-hasta que toda la lista esté ordenada.-Es simple pero ineficiente para-listas grandes.", 679, 56 + (300 - 20*6 + 43)/2)
        drawDescription("Insertion Sort ordena la lista insertando-cada elemento en su posición correcta en-la lista ordenada, uno a uno.-Es eficiente para listas-pequeñas y casi ordenadas.", 1110, 56 + (300 - 20*5 + 43)/2)
        drawDescription("Merge Sort divide, ordena y fusiona listas-para obtener una lista ordenada. Es eficiente-y funciona bien para listas de-cualquier tamaño.", 470, 414 + (300 - 20*4 + 43)/2)
        drawDescription("Quicksort selecciona un 'pivote', reorganiza-la lista para tener elementos más-pequeños a la izquierda y elementos más-grandes a la derecha del pivote, luego-repite este proceso recursivamente.-Es rápido pero puede ser lento-en listas casi ordenadas.", 897, 414 + (300 - 20*7 + 43)/2)

    def isOrdered(self, arr):
        for i in range(len(arr) - 1):
            self.sorting(arr, i, i + 1)
            if arr[i] > arr[i + 1]:
                return False
        return True

    def bubbleSort(self, arr):
        for i in range(len(arr) - 1, 0, -1):
            for v in range(i):
                self.sorting(arr, v, v + 1)
                if arr[v+1] < arr[v]:
                    arr[v], arr[v+1] = arr[v+1], arr[v]
                    self.sorting(arr, v, v + 1)
        self.isOrdered(arr)

    def selectionSort(self, arr):
        smallest = None
        for i in range(len(arr)):
            smallest = i
            for v in range(i + 1, len(arr)):
                self.sorting(arr, smallest, v)
                if arr[smallest] > arr[v]:
                    smallest = v
            self.sorting(arr, i, smallest)
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.sorting(arr, smallest, i)
        self.isOrdered(arr)

    def insertionSort(self, arr):
        for i in range(1, len(arr)):
            for v in range(i):
                self.sorting(arr, i, v)
                if arr[i] < arr[v]:
                    arr.insert(v, arr[i])
                    arr.pop(i+1)
                    self.sorting(arr, v, v+1)
                    break
        self.isOrdered(arr)

    def mergeSort(self, arr, OrgArr, Offset=0):
        mid = len(arr) // 2
        if mid == 0:
            return arr
        lower = self.mergeSort(arr[0:mid], OrgArr, Offset)
        upper = self.mergeSort(arr[mid:], OrgArr, Offset + mid)
        i = 0
        v = 0
        while v < len(lower):
            self.sorting(OrgArr, Offset + v, Offset + mid + i)
            if lower[v] > upper[i]:
                lower.insert(v, upper[i])
                OrgArr.insert(v + Offset, upper[i])
                OrgArr.pop(i + mid + Offset + 1)
                self.sorting(OrgArr, Offset + v, Offset + v + 1)
                i += 1
            if i == len(upper):
                break
            v += 1
        if i != len(upper):
            lower += upper[i:]

        return lower

    def quickSort(self, arr, start, end):
        if end - start <= 1:
            return None
        pivotI = randint(start, end - 1)
        pivotV = arr[pivotI]
        self.sorting(arr, pivotI, start)
        arr.insert(start, arr[pivotI])
        arr.pop(pivotI + 1)
        pivotI = start
        self.sorting(arr, pivotI, pivotI + 1)
        for i in range(start + 1, end):
            self.sorting(arr, i, pivotI)
            if arr[i] < pivotV:
                arr.insert(pivotI, arr[i])
                arr.pop(i + 1)
                pivotI += 1
                self.sorting(arr, i, pivotI)
        self.quickSort(arr, start, pivotI)
        self.quickSort(arr, pivotI + 1, end)


def getArgs():
    for i, v in enumerate(argv):
        if v in ["am", "arrMax"]:
            Configuration.arrRange = (1, int(argv[i + 1]) + 1)
        if v in ["delay", "d"]:
            Configuration.sleepTime = float(argv[i + 1])
        if v in ["bw", "barWidth"]:
            Configuration.barWidth = int(argv[i + 1])


def main():
    getArgs()
    window = Pantallaball()
    window.start()
    window.menu()
    window.update()
    window.checkEventsMenu()


if __name__ == "__main__":
    main()
