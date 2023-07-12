---
title: spss和Excel数据格式转mplus格式数据（在线）
date: 2023-07-08 14:00:37
tags: [spss,mplus]
---

很多时候我们需要转换数据格式，比如SPSS转Excel， SPSS转Mplus数据等，
为了方便广大童鞋的数据分析工作， 我们做了一个数据格式转换的工具，
开发了1个月终于上线， 大家不用登陆就可以免费使用， 并且数据尽在你本地浏览器保存，
并没有上传到后台服务器， 打开网页以后断网也可以使用， 所以最大限度保证了你的数据安全性！

这个工具的主要用途是将Excel或者spss数据转换为mplus可用的数据格式。

<!-- more -->


# Excel和SPSS转MPLUS

dat是Mplus默认使用的数据格式， 其实dat是一个文本文件，
数据的列与列用Tab键隔开。同时输出了变量名，方便你在muplus中调用数据。

## 1 输入数据（目前支持xls/xlsx/sav格式的数据)

{% raw %}


<div style="width=100%;border-style: dotted;border-width: 2px;">
<label for="e2dfiles" class="form-label button">选择Excel/SPSS文件</label>
<input id="e2dfiles" class="form-control" type="file" accept=".xls,.xlsx,.sav" onchange="read(this)"  >

<div id="sheetSelector" style="display:none" class="form-group">
    <label for="sheet">选择工作表</label>
    <select class="form-control" id="sheet" >
    </select>
</div>
</div>
{% endraw %}

## 2 选择变量

{% raw %}

<div id="variables" style="border-style: dotted;border-width: 2px; ">
</div>

{% endraw %}

## 3 设置缺失值

{% raw %}
<div style="border-style: dotted;border-width: 2px;">
<label for="mvalue" class="form-label">缺失值：</label>
<input class="form-control" id="mvalue" value="-999" oninput="genCode()">
</div>
{% endraw %}


## 4 下载Mplus数据（dat格式）

{% raw %}
<div style="border-style: dotted;border-width: 2px;">
<label for="mpluscode">Mplus代码：</label>
<textarea id="mpluscode" class="form-control" rows="10"></textarea>
</div>

<button class="form-control" onclick="downloadData()">下载数据</button>
{% endraw %}

# 下载N2mplus

https://www.danielsoper.com/n2mplus/


{% raw %}
<div>
<script src="https://unpkg.com/xlsx/dist/xlsx.full.min.js"></script>
<script id="e2dfiles" src="./vender/savvy/index.js"></script>


<style>

</style>
<script>
    let JSONData;
    let CleanData;
    function read(iptEle){
        console.log(iptEle.files[0])
        let file = iptEle.files[0];
        $('#filename').val(file.name);
        console.log(file.name)
        if(file.name.endsWith('.xls') | file.name.endsWith('.xlsx')){
            $('#sheetSelector').show();
            console.log('excel file');
            excel2json(iptEle);
        }
        if(file.name.endsWith('.sav')){
            $('#sheetSelector').hide();
            sav2json(iptEle);
        }
        
    }
    

</script>
<script>
    function getEmptyName(cols){
        let name = '__EMPTY'
        let i=0;
        while(cols.includes(name)){
            i++;
            name = `__EMPTY_${i}`
        }
        return name
    }
    function excel2json(iptEle){
        console.log(window.XLSX);
        console.log(iptEle)
        let reader = new FileReader();
        reader.readAsBinaryString(iptEle.files[0]);
        reader.onload = event=>{
            let data = event.target.result;
            let workbook = XLSX.read(data,{type:"binary"});
            console.log(workbook.SheetNames);
            let jdata = {};
            let shOpts = '';
            workbook.SheetNames.forEach(sheet => {
                let cols = []
                let worksheet = workbook.Sheets[sheet];
                let ref = worksheet["!ref"]
                if(ref==undefined){
                    cols=[]
                    jdata[sheet] = {data: [], cols: cols}
                }else{
                    let range = XLSX.utils.decode_range(worksheet["!ref"]);
                    let rowObject = XLSX.utils.sheet_to_row_object_array(worksheet);
                    
                    for(let c=range.s.c; c<=range.e.c; c++){
                        let cell = worksheet[XLSX.utils.encode_cell({r:range.s.r, c:c})];
                        console.log({r:range.s.r, c:c, cell, })
                        if(cell==undefined){
                            cols.push(getEmptyName(cols))
                        }else{cols.push(cell.v)}
                    }
                    jdata[sheet] = {data: rowObject, cols: cols};
                    
                }
                shOpts += `<option value="${sheet}">${sheet}</option>`;
            });
            $('#sheet').empty();
            $('#sheet').append(shOpts);
            $('#sheet').off('change');
            $('#sheet').change(function(){
                console.log(this.value);
                changeSheet(this.value)
            });
            JSONData = {
                sheets: workbook.SheetNames,
                data: jdata,
            }
            changeSheet(JSONData.sheets[0]);
            CleanData = JSONData.data[JSONData.sheets[0]];
            console.log(JSONData)
        }
    }
    function sav2json(iptEle){
        const file = iptEle.files[0];
        const reader = new FileReader();
        const parser = new savvy.SavParser();
        reader.onload = function(){
            let cols=[];
            let data = reader.result;
            console.log(data)
            parser.all(new savvy.Feeder(data)).then(parsed=>{
                console.log(parsed);
                parsed.headers.forEach(head=>{
                    cols.push(head.name);
                })
                JSONData = {
                    sheets: ['spss'],
                    data: {
                        spss: {
                            cols: cols,
                            data: parsed.rows,
                        },
                    },
                }
                console.log(JSONData)
                changeSheet(JSONData.sheets[0])
            })
        }
        reader.readAsArrayBuffer(file);
    }
    function changeSheet(name){
        CleanData = JSONData.data[name];
        let options = '';
        CleanData.cols.forEach(c=>{
            options += `
            <label class="form-check-label" style="margin-left: 5px; border-bottom: 1px dotted #d7ecff;"><input class="varnames" checked type="checkbox" value="${c}">${c}</label>
            `;
        })
        $('#variables').empty();
        $('#variables').append(options);
        genCode();
        $('.varnames').change(ent=>{
            genCode();
        })
    }
    function getSelectedVars(){
        let selected = [];
        $('#variables').find('input').each((i, el)=>{
             el = $(el);
            if(el.is(':checked')){
                selected.push(el.val())
            }
        })
        return selected
    }
    function genCode(){
        let selected = getSelectedVars();
        let mv = $('#mvalue').val()
        let names = selected.join(' ')
        let code = `
DATA:
    FILE IS data.dat;
VARIABLE:
    MISSING ARE ALL(${mv});
    NAMES ARE ${names};`
    $('#mpluscode').empty()
    $('#mpluscode').append(code)
    }
    function _download(filename, text) {
        var element = document.createElement('a');
        element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        element.setAttribute('download', filename);
        element.style.display = 'none';
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    }
    function downloadData(){
        console.log({CleanData, });
        if(!CleanData){
            alert("没有数据")
            return
        }
        let selected = getSelectedVars();
        if(!selected.length){
            alert("没有变量")
            return
        }
        let tab = '	';
        let allData = '';
        let miss = $('#mvalue').val()
        CleanData.data.forEach(row=>{
            if(!!allData){
                allData += '\n';
            }
            let rowData = [];
            selected.forEach(col=>{
                let val;
                if(row instanceof Map){
                    val = row.get(col)
                }else{
                    val = row[col]
                }
                if(val==undefined){
                    val = miss;
                }
                rowData.push(val)
            })
            allData += rowData.join(tab)
        })
        _download('data.dat', allData)
    }
</script>
</div>
{% endraw %}
