from datetime import datetime
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
from prophet.diagnostics import performance_metrics
from prophet.serialize import model_to_json, model_from_json
import streamlit as st


def prepare_future_data():

    with open("data/serialized_model.json", "r") as fin:
        m = model_from_json(fin.read())

    sao_goncalo_data = pd.read_csv("data/data.csv")
    sao_goncalo_data = sao_goncalo_data[sao_goncalo_data["Rio"] != "lagoa dos patos"]
    sao_goncalo_data["ds"] = pd.to_datetime(sao_goncalo_data["ds"], format="%d/%m/%Y %H:%M:%S")
    #sao_goncalo_data["ds"] = sao_goncalo_data["ds"].dt.strftime("%d-%m-%Y, %H:%M:%S")
    
    pos_wind = pd.read_csv("data/wind.csv")
    pos_wind["ds"] = pd.to_datetime(pos_wind["ds"], format="%d/%m/%Y %H:%M:%S")
    #pos_wind["ds"] = pos_wind["ds"].dt.strftime("%d-%m-%Y, %H:%M:%S")
    sao_goncalo_data = pd.merge(sao_goncalo_data, pos_wind, on="ds")
    future = m.make_future_dataframe(periods=44, freq="h")
    future["pos_wind"] = pos_wind["pos_wind"]
    forecast = m.predict(future)
   
    forecast = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]
    forecast_ = forecast.rename(
        columns={
            "ds": "Date/Hour",
            "yhat_lower": "Projection Lower",
            "yhat": "Projection",
            "yhat_upper": "Projection Upper",
        },
        errors="raise",
    )

    hour_now = datetime.now()
   
    forecast_ = forecast_[forecast_['Date/Hour'] > hour_now]

    return plot_plotly(m, forecast), forecast_


def main():
    st.title("Flood São Gonçalo")

    if st.button("Predict"):
        result = prepare_future_data()
        st.plotly_chart(result[0], use_container_width=True)
        st.table(result[1].head(10))


if __name__ == "__main__":
    main()
