public class Toy implements Comparable<Toy> {
    private final int id;
    private final String name;
    private int weight;
    private int quantity;
    public Toy(int id, String name, int quantity, int weight) {
        this.id = id;
        this.name = name;
        this.quantity = quantity;
        this.weight = weight;
    }
    public int getId() {
        return id;
    }
    public String getName() {
        return name;
    }

    public int getWeight() {
        return weight;
    }
    // Метод изменения вероятности выпадения
    public void setWeight(int weight) {
        this.weight = weight;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @Override
    public String toString() {
        return "Игрушка ID №" + id +
                ", наименование: " + name +
                ", вес: " + weight + ", кол-во: " + quantity;
    }
    @Override
    public int compareTo(Toy o) {
        if (weight == o.getWeight()) return 0;
        else if (weight < o.getWeight()) return -1;
        return 1;
    }
}
