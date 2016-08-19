package ac.cr.tec.main;

import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        RNG rng = new RNG();
        Archivo archivo = new Archivo();
        try {
            archivo.abrir("java.txt");
            for (int i = 0; i < 1000000; i++) archivo.escribir(rng.generateRandom());
            archivo.cerrar();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
