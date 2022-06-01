from queue import Empty
import PySimpleGUI as sg
import pdfFunctions as pydf

HomeLayout = [
    [sg.Button("Merge Docs"), sg.Button("Remove Pages")]
]

HomeWindow = sg.Window("Home", HomeLayout)

MergeDocsActive = False
# RemovePagesActive = False

MergeFileList = []

while True:
    event, values = HomeWindow.read()
    
    if event == "Merge Docs" and not MergeDocsActive:
        print("Merge Docs Button has been clicked !")
        Row1 = [
            sg.Text("Select File: "), 
            sg.In(size = (30, 5) ,enable_events=True, key="_FILECHOSEN_"), 
            sg.FileBrowse(), 
            sg.Button("Add", enable_events=True, key="_ADDFILE_"),
            sg.Button("Remove", enable_events=True, key="_REMOVEFILE_")
        ]
        MergeDocsLayout = [
            [Row1],
            [sg.Text("Selected Files")],
            [sg.Listbox(values=[], size=(65, 5), key="_FILELIST_")],
            [sg.Button("Merge",enable_events=True ,key="_MERGEFILE_")]
        ]

        HomeWindow.hide()
        MergeDocsWindow = sg.Window("Merge Docs", MergeDocsLayout)
        MergeDocsActive = True

        while True:
            event2, values2 = MergeDocsWindow.read()
            # print(event2)
            if event2 == "_ADDFILE_":
                fileDirectory = values2["_FILECHOSEN_"]
                MergeFileList.append(fileDirectory)
                MergeDocsWindow["_FILELIST_"].update(MergeFileList)

            elif event2 == "_REMOVEFILE_":
                chosenFile = values2["_FILELIST_"]
                print("File to be removed: ", chosenFile)
                if chosenFile == []:
                    sg.popup("Please select a file to remove")
                else:
                    chosenFile = chosenFile[0]
                    MergeFileList.remove(chosenFile)
                    MergeDocsWindow["_FILELIST_"].update(MergeFileList)
            elif event2 == "_MERGEFILE_":
                try:
                    print(MergeFileList)
                    pydf.merge(MergeFileList)
                except:
                    sg.popup("Error Occurred")
                MergeFileList.clear()
                MergeDocsWindow["_FILELIST_"].update(MergeFileList)

            elif event2 == sg.WIN_CLOSED:
                MergeFileList.clear()
                MergeDocsActive = False
                MergeDocsWindow.close()
                HomeWindow.UnHide()
                break
        

    if event == sg.WIN_CLOSED:
            HomeWindow.close()
            break
    # if event == "Remove Pages" and not RemovePagesActive:
    #     print("Remove Pages Button has been clicked !")
    #     RemovePagesLayout = [
    #         [sg.Text("Remove Pages Window")]
    #     ]
    #     RemovePagesWindow = sg.Window("Remove Pages", RemovePagesLayout)
    #     RemovePagesActive = True
   
    # if RemovePagesActive:
    #     event3, values3 = RemovePagesWindow.read()

    #     if event3 == sg.WIN_CLOSED:
    #         RemovePagesActive = False
    #         RemovePagesWindow.close()
    #         break
    

    
