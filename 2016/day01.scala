object Day01{

    case class Step(x: Int, y: Int, phi: Int) {
        def L(): Step = this.copy(phi = (phi + 3) % 4)
        def R(): Step = this.copy(phi = (phi + 1) % 4)

        def step(l: Int): Step =
            this.phi match {
                case 0 => this.copy(y = y + l)
                case 1 => this.copy(x = x + l)
                case 2 => this.copy(y = y - l)
                case 3 => this.copy(x = x - l)
            }
    }

    def main(args: Array[String]){
        val directions: Array[(String, String)] = scala.io.Source.fromFile("input1.txt").mkString.split(',').map(_.trim.splitAt(1))

        val start: Step = Step(0, 0, 0)

        val end = directions.foldLeft(start) {
            case (pos, ("R", d)) => pos.R().step(d.toInt)
            case (pos, ("L", d)) => pos.L().step(d.toInt)
        }

        println(end)
    }

}
