from pathlib import Path
import numpy as np

def read_baby_names(
        file: Path
        ) -> list[list[str, str]]:
    """_summary_

    Args:
        file (Path): path to file

    Returns:
        list[list[str, str]]: baby name data
    """
    if type(file) is str:
        file = Path(file)
    text = file.read_text()
    data = [x.split(",") for x in text.split("\n")]
    data = [x for x in data if len(x) >= 2]
    return(data)


def test_dev_train_split(
        feature_list: list,
        props: tuple[float, float, float] = (0.6, 0.2, 0.2)
        ) -> tuple[list, list, list]:
    """_summary_

    Args:
        feature_list (list): feature list
        props (tuple[float, float, float], optional): 
            Proportional split. Defaults to (0.6, 0.2, 0.2).

    Returns:
        tuple[list, list, list]: Train, Dev, Test data
    """
    n_data = len(feature_list)

    n_train = int(np.round(n_data * props[0]))
    n_test = int(np.round(n_data * props[2]))
    n_dev = n_data - n_train - n_test

    all_indicies = list(range(n_data))

    train_idx = np.random.choice(
        all_indicies, 
        size = n_train,
        replace=False
        )

    remaining_idx = [idx for idx in all_indicies if idx not in train_idx]
    
    test_idx = np.random.choice(
        remaining_idx,
        size = n_test,
        replace = False
    )

    dev_idx = [idx for idx in remaining_idx if idx not in test_idx]

    train_data = [feature_list[idx] for idx in train_idx]
    dev_data = [feature_list[idx] for idx in dev_idx]
    test_data = [feature_list[idx] for idx in test_idx]


    return (train_data, dev_data, test_data)


