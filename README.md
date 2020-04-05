done
    val u = Json.obj("$set" -> Json.obj(ReplayDeadLetter.Status -> Status.Done))

    with error
        val u = Json.obj(fields = "$push" -> Json.obj(ReplayDeadLetter.Errors -> exception.getMessage))

<<<<<<< HEAD
failed
      "$set" -> Json.obj(ReplayDeadLetter.Status -> Status.Failed),
      "$push" -> Json.obj(ReplayDeadLetter.Errors -> exception.getMessage))
=======
# Winning Plan
[![Plain](https://i.ibb.co/DzG2QJG/Screen-Shot-2020-03-24-at-15-05-50.png "Plain")](https://i.ibb.co/DzG2QJG/Screen-Shot-2020-03-24-at-15-05-50.png "Plain")

# Initialize
- ❯ `grakn server start`
- ❯ `grakn console --keyspace conversations_graph --file /Users/Zvi/Desktop/FinalProject/Final-Project/init_graph.gql`
- ❯ `grakn console --keyspace conversations_graph`
- ❯ `match $user isa user; get;`
>>>>>>> 9f6025ea873e7dfafefa82d2471e4a574a55ef91
