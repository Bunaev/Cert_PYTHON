import java.util.ArrayList;
import java.util.Scanner;

public class Store {
    public static void main(String[] args) {
        ArrayList<Toy> toys = new ArrayList<>();
        Ruffle ruffle = new Ruffle();
        // Заполняем магазин призовыми игрушками.
        toys.add(new Toy(1, "Кукла 'Dolly'", 50, 60));
        toys.add(new Toy(2, "Машинка 'Monster Truck'", 30, 30));
        toys.add(new Toy(3, "Конструктор 'LEGO City'", 20, 20));
        // Реализовал небольшой интерфейс, дабы удобнее быо вызывать метод.
        // Если в призовом фонде нет игрушек - будет осуществлен автоматический выход из цикла.
        System.out.print("Привет! Сыграем? Да/Нет: ");
        try {
            String answer = inputAnswer();
            while (answer.contains("д")) {
                Toy prize = ruffle.rafflePrizes(toys);
                if (prize == null) {
                    System.out.print("Вы ничего не выйграли, повезет в другой раз! Сыграем еще? Да/Нет: ");
                    answer = inputAnswer();
                } else {
                    System.out.print("Поздравляем! Вы выйграли: " + prize.getName() + "! Хотите еще сыграть? Да/Нет: ");
                    if (toys.isEmpty()) {
                        System.out.println("Все призы разыграны!");
                        break;
                    } else {
                        answer = inputAnswer();
                    }
                }
            }
        } catch (Exception e) {
            System.out.println("Вы ввели неверное значение.");
        }
        System.out.println("Пока-пока! Приходите еще!");
    }
    // Метод ввода с отработкой исключений
    public static String inputAnswer() throws InvalidInputException {
        Scanner scanner = new Scanner(System.in);
        String answer = scanner.next();
        if (!answer.contains("д") && !answer.contains("н")){
            throw new InvalidInputException();
        }
        else {
            return answer;
        }
    }
}
