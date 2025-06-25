* Encoding: UTF-8.
*© 2021 by Ruben Geert van den Berg - www.spss-tutorials.com.

begin program python3.
import SpssClient
SpssClient.StartClient()
try:
    oDoc = SpssClient.GetDesignatedOutputDoc()
    oItems = oDoc.GetOutputItems()
    itemCount = oItems.Size()
    for ind in range(itemCount):
        oItem = oItems.GetItemAt(itemCount - ind - 1)
        if oItem.GetType() == SpssClient.OutputItemType.PIVOT and oItem.GetSubType() == 'Factor Correlation Matrix' and oItem.GetProcedureName() == 'Factor Analysis':
            pTable = oItem.GetSpecificType()
            pTable.SetUpdateScreen(False)
            pManager = pTable.PivotManager()
            
            #1. REPLACE ROWLABELS
            rowLabels = pTable.RowLabelArray()
            for rowInd in range(rowLabels.GetNumRows()):
                newLabel = 'Factor ' + str(rowInd + 1)
                rowLabels.SetValueAt(rowInd,1,newLabel)
                
            #2. REPLACE COLLABELS
            colLabels = pTable.ColumnLabelArray()
            for colInd in range(colLabels.GetNumColumns()):
                oldLabel = colLabels.GetValueAt(1,colInd)
                colLabels.SetValueAt(1,colInd,str(colInd + 1))
                
            #3. REMOVE REDUNDANT CORRS
            dCells = pTable.DataCellArray()
            for row in range(dCells.GetNumRows()):
                for col in range(dCells.GetNumColumns()):
                    if row < col: #HIDE EVERYTHING ABOVE DIAGONAL
                        dCells.SetValueAt(row,col,'')
                        dCells.SetTextHiddenAt(row,col,True)
                    elif row == col: #SET DIAGONAL TO DASHES
                        dCells.SetValueAt(row,col,'-')
                    else: #UNDER DIAGONAL, SET 2 DECIMAL PLACES
                        dCells.SetHDecDigitsAt(row,col,2)
            pTable.SetUpdateScreen(True)
            break #STOP LOOPING THROUGH OUTPUT IF COR TABLE HAS BEEN FOUND
finally:
    SpssClient.StopClient()
end program.
