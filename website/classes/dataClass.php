 <?php
    
    require "../config.php";
    

    class DataClass
    {
        private $Number;
        private $Comment;
        private $Type;
        private $Researchs;
        private $Score;
        private $Source;


        public static function getData()
        {
            try {
                $conn = new PDO("mysql:host=" . $GLOBALS['SERVER'] . "; dbname=" . $GLOBALS['DB']);
                $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                $stmt = $conn->prepare("SELECT * FROM teldata");
                $stmt->execute([]);
                $array = array();
                while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                    array_push($array, array(
                        "Number" => $row['number'],
                        "Comment" => $row['comment'],
                        "Type" => $row['type'],
                        "Researchs" => $row['researchs'],
                        "Score" => $row['score'],
                        "Source" => $row['source']
                    ));
                }
                return $array;
            } catch (PDOException $e) {
                echo $e->getMessage();
                return array();
            }
        }
    }

    


    ?>