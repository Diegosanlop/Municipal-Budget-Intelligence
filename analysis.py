import pandas as pd


def main():
    df = pd.read_csv("data.csv")
    df["variance"] = df["actual"] - df["budget"]
    df["execution_rate"] = (df["actual"] / df["budget"]) * 100
    print(df)


if __name__ == "__main__":
    main()
