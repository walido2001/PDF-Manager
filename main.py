import PySimpleGUI as sg

HomeLayout = [
    [sg.Button("Merge Docs"), sg.Button("Remove Pages")]
]

HomeWindow = sg.Window("Home", HomeLayout)

MergeDocsActive = False
RemovePagesActive = False

while True:
    event, values = HomeWindow.read()
    
    if event == "Merge Docs" and not MergeDocsActive:
        print("Merge Docs Button has been clicked !")
        MergeDocsLayout = [
            [sg.Text("Select File: "), sg.In(size=(10, 1)), sg.FileBrowse(), sg.Button("Add File")],
            [sg.Text("Selected Files: ")]
        ]
        MergeDocsWindow = sg.Window("Merge Docs", MergeDocsLayout)
        MergeDocsActive = True

    if event == "Remove Pages" and not RemovePagesActive:
        print("Remove Pages Button has been clicked !")
        RemovePagesLayout = [
            [sg.Text("Remove Pages Window")]
        ]
        RemovePagesWindow = sg.Window("Remove Pages", RemovePagesLayout)
        RemovePagesActive = True

    if MergeDocsActive:
        event2, values2 = MergeDocsWindow.read()

        if event2 == sg.WIN_CLOSED:
            MergeDocsActive = False
            MergeDocsWindow.close()
            break
   
    if RemovePagesActive:
        event3, values3 = RemovePagesWindow.read()

        if event3 == sg.WIN_CLOSED:
            RemovePagesActive = False
            RemovePagesWindow.close()
            break
    

    if event == sg.WIN_CLOSED:
        HomeWindow.close()
        break
