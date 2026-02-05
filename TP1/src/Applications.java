import javax.xml.ws.Endpoint;

public class Applications {
    public static void  main(String[]args) {
        System.out.println("Début de déploiement de mon service" );
        String url = "http://localhost:8888/";
        Endpoint.publish(url, new Monserviceweb());
        System.out.println("Le service web est déployé");
    }
}
