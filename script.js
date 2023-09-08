function colorNuc(idName, Name2){
  var text = document.getElementById(idName);
  var str = text.innerHTML,
      reg = /red|blue|green|black|#ccff00/ig;

  var toStr = String(reg);
  var color = (toStr.replace('\/g', '|')).substring(1);

  var colors = color.split("|");

  if (colors.indexOf("red") > -1) {
      str = str.replace(/T/g, '<span style="color:red;">T</span>');
  }

  if (colors.indexOf("blue") > -1) {
      str = str.replace(/C/g, '<span style="color:blue;">C</span>');
  }

  if (colors.indexOf("green") > -1) {
      str = str.replace(/A/g, '<span style="color:green;">A</span>');
  }

  if (colors.indexOf("black") > -1) {
      str = str.replace(/G/g, '<span style="color:black;">G</span>');
  }
  if (colors.indexOf("#ccff00") > -1) {
    str = str.replace(/_/g, '<span style="color:#ccff00;">-</span>')
  }
  document.getElementById(Name2).innerHTML = str;
 }


colorNuc("content3", "updated3")
colorNuc("content", "updated")
colorNuc("content2", "updated2")