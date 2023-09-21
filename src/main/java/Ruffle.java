import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

public class Ruffle {
    Random rand = new Random();
    // Класс и метод raffle созданы только для самого розыгрыша и разгрузки клиентского кода.
    // Количество игрушек в магазине уменьшается с каждым выйгрышем,
    // если кол-во достигает "0" - игрушка удаляется из призового фонда.
    // Запись в файл ведется о каждом выйгрыше и о кол-ве игрушек на остатках.
    public Toy rafflePrizes(ArrayList<Toy> toys) {
        int choice = rand.nextInt(0, 101);
        for (Toy toy : toys) {
            if (choice <= toy.getWeight()) {
                try (FileWriter writer = new FileWriter("Result.txt", true) ) {
                    toy.setQuantity(toy.getQuantity() - 1);
                    if (toy.getQuantity() == 0) {
                        toys.remove(toy);
                    }
                    writer.write(toy.getId() + " - " + toy.getName() + "; В розыгрыше еще участвуют: " + toy.getQuantity() + " шт.\n");
                    return toy;
                } catch (IOException e) {
                    System.out.println("Не удалось записать файл.");
                }
            } else {
                choice = rand.nextInt(0, 101);
            }
        }
        return null;
    }
}
