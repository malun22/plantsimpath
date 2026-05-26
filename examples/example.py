from plantsimpath import PlantsimPath


def make_path() -> None:
    station = PlantsimPath(".Models.Model.Station")
    station_wo_dot = PlantsimPath("Models.Model.Station")

    print(
        f'Do Plantsim path always begin with a "."? {"Yes" if station == station_wo_dot else "No"}'
    )

    attribute_div = station / "ProcTime"
    attribute_add = station + "ProcTime"
    attribute_init = PlantsimPath(station, "ProcTime")

    print(f"Are all paths the same? {attribute_div == attribute_add == attribute_init}")

    model = station.parent()
    is_child = station.is_child_of(model)
    print(f"Is {station} a child of {model}? {'Yes' if is_child else 'No'}")

    system_path = station.to_path()
    print(f"{station} is located at {system_path}")

    system_path = station.to_object_path()
    print(f"{station}'s meta data is located at {system_path}")

    system_path = model.to_folder_path()
    print(f"{model}'s meta data is located at {system_path}")

    table_path = PlantsimPath('.Models.Model.Table["ColumnIndex",10]')
    object_in_table = table_path / "ProcTime"

    print(
        f"Is {object_in_table} a child of {table_path}? {object_in_table.is_child_of(table_path)}"
    )


if __name__ == "__main__":
    make_path()
