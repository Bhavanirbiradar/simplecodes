public class MoveAllX {
   
    public static void moveall(String str,int idx,int count,String newstring){
        if(idx==str.length()){
            for(int i=0;i<count;i++){
                newstring+="x";
            }
            System.out.println(newstring);
            return;
        }
        char curr=str.charAt(idx);
        if(curr=='x'){
            count++;
            moveall(str,idx+1,count,newstring);
        }
        else{
            newstring+=curr;
            moveall(str,idx+1,count,newstring);
        }
    }
    public static void main(String args[]){
        String str="abxcdxxx";
        moveall(str,0,0," ");
    }

    
}
