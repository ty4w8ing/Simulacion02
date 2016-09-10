package ac.cr.tec.main;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Archivo {

    File archivo;
    FileWriter fw;
    BufferedWriter bw;

    public void abrir(String nombre) throws IOException {
        try {
            archivo = new File(nombre);
            if (!archivo.exists()) archivo.createNewFile();

            fw = new FileWriter(archivo.getAbsoluteFile(), false);
            bw = new BufferedWriter(fw);

        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public void escribir(Double texto){
        try {
            bw.write(String.format("%.10f", texto)+'\n');
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void cerrar (){
        try {
            bw.close();
            fw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
