//Result Genie JSON Generation v0.0.1
[
  '{{repeat(1)}}',
  {
    index:'{{(index())}}',
    name: '{{firstName()}} {{surname()}}',
    USN: function(tags){
      var usn_name = '4MH11EC';
      var usn = tags.index().toString();
      switch(usn.length) {
        case 1:
          usn=usn_name+'00'+usn;
          break;
        case 2:
          usn=usn_name+'0'+usn;
          break;
        default:
          usn=usn_name+usn;
      }
      return usn;
    },
    semester: 1,
    resultClass:"",
    subject: [
      '{{repeat(6)}}',
      {
        id:'{{(index()+1)}}',
        name:function(tags){
          var list =["Sem1_Subject1","Sem1_Subject2","Sem1_Subject3","Sem1_Subject4","Sem1_Subject5","Sem1_Subject6"];
          var num = '{{index()}}' ;
          return list[tags.index()];
        },
      internalMarks: '{{integer(1, 25)}}',
      externalMarks: '{{integer(1, 100)}}',
      totalMarks: function(tags){ return this.internalMarks + this.externalMarks; },
        subjectCode:'{{index()}}',
      result: function(tags){
       if(this.totalMarks <50)
         return "FAIL";
       else
         return "PASS";
      }
    }],
    
    
    result:function(tags){
      var totalMarks=0;
      for (var i = 0; i <  this.subject.length; i++) { 
      totalMarks += this.subject[i].totalMarks;
	} 
       for (i = 0; i <  this.subject.length; i++) { 
       if(this.subject[i].result == "FAIL")
         return "FAIL";
	} 
      totalMarks = totalMarks/625 *100;
       if(totalMarks <35)
         return "FAIL";
       else if (totalMarks >= 35 && this.totalMarks<50)
         return "PASS";
       else if (totalMarks >=50  && this.totalMarks<60)
         return "SECOND CLASS";
        else if (totalMarks >=60  && this.totalMarks<70)
         return "FIRST CLASS";
        else
         return "FIRST CLASS WITH DISTINCTION";
    }    
  }
]


 
