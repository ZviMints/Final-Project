done
    val u = Json.obj("$set" -> Json.obj(ReplayDeadLetter.Status -> Status.Done))

    with error
        val u = Json.obj(fields = "$push" -> Json.obj(ReplayDeadLetter.Errors -> exception.getMessage))

failed
      "$set" -> Json.obj(ReplayDeadLetter.Status -> Status.Failed),
      "$push" -> Json.obj(ReplayDeadLetter.Errors -> exception.getMessage))