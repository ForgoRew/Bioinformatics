import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

@interface RequestForEnhancement {
    int id();
    String engineer () default "[Unasigned]";
    String value();
}

public class PokJava{
    @Deprecated
    public static void main(String[] args){
        String s = "Hello World!";
        Object o = (Object) s;
        String s2 = (String) o;
        Object o2 = new ArrayList<>();
        ArrayList<Object> l3 = (ArrayList) o2;
        // String s3 = (String) o2;
        System.out.println(s);
        System.out.println(o);
        System.out.println(s2);

        // List<? extends String> ls = new List() {};

        //var a = Collections.<Integer>emptyList();
        //a.add(Integer.parseInt("1")); 
        //a.add("Hi");
        var l1 = new ArrayList<Integer>();
        var l2 = new ArrayList<String>();
        if (l1.getClass() == l2.getClass()){
            return;
        };
    }

    private String id() {
        return null;
    }

    private String id() {
        return null;
    }
}