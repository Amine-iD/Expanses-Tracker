function loadData(itemData , categoryData){
    items = JSON.parse(itemData)
    categories = JSON.parse(categoryData)
}

function addRow(){
    // Adding the <td> of categories
        let newRow = '<td class="py-2 px-4 border-b border-gray-200" ><select name="category" id="category">'
        for(i=0 ; i<categories.length ; i++){
            newRow += `<option value=" ${categories[i]}  ">` +categories[i]+'</option>'
            }
        newRow+= '</select></td>' 
    // Adding the <td> of items
        newRow+= '<td class="py-2 px-4 border-b border-gray-200" ><input class = "input" name="item" id="item"></input></td>'
    // Adding the <td> of Description
        newRow+= '<td class="py-2 px-4 border-b border-gray-200" title="Description"> <textarea  name="Description" class = "w-full h-24 bg-white border border-gray-300 rounded py-1 px-2 resize-none"  id="xpanse-description"></textarea></td>'
    
    newRow += '<td class="py-2 px-4 border-b border-gray-200" ><input type="date" name="" id=""></td>'
    
    const tbody = document.querySelector(".exp-table tbody")//when I did it using the `id` of the table it didn't stay working for too long!!
    let tr = document.createElement('tr')
    tr.classList.add('hover:bg-gray-100','cursor-pointer','row')
    tr.innerHTML = newRow
    tbody.appendChild(tr)

    let table = document.querySelector('.exp-table')
    let selected = null ;
    table.addEventListener('click' ,function(e){
        const clickedRow = e.target.closest('tr')
        if (e.target.matches('textarea , input  , option , select')) // Prevent the selection when filling the table
            return;

        if (clickedRow){
            if (clickedRow !== selected){
                if (selected){ 
                    console.log('Clicke R0w != selected , selected == 1')
                    selected.classList.remove('selected');
                    selected = clickedRow;
                    clickedRow.classList.add('selected');
                    return;
                }
                else{
                    selected = clickedRow;
                    selected.classList.add('selected')
                    console.log(' selected is NULL')
                    return;
                }
            }
            if (clickedRow == selected){ // I don't know why the `else` statement here causes a bug (the toggling gets deactivated , and the selected remains unchanged even after clicking twice ) 
                clickedRow.classList.toggle('selected')
                console.log('in the second condition')
                return;
            }
        }
    })
    // if The user clicks outside of the table
    document.addEventListener('click' , function(e){
        if (!table.contains(e.target)){
            if (selected){
                selected.classList.remove('selected')
                selected = null;
            }
        }
    })
    }

function deleteRow(){
   let selectedRow = document.querySelector('.selected')
   if (selectedRow) selectedRow.remove();
}
