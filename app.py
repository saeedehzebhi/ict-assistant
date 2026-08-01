
import streamlit as st
import pandas as pd

# -----------------------------
# تنظیمات صفحه
# -----------------------------
st.set_page_config(
    page_title="سامانه اطلاعات روستاها",
    page_icon="🏘️",
    layout="centered"
)

# -----------------------------
# خواندن فایل Excel
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_excel("C:/Users/AllUser/Desktop/ICT-streamlit/villages.xlsx")


df = load_data()

# -----------------------------
# عنوان
# -----------------------------
st.title("🏘️ سامانه اطلاعات روستاها")
st.write("نام روستا را وارد کنید تا اطلاعات آن نمایش داده شود.")

# -----------------------------
# ورود نام روستا
# -----------------------------
village_name = st.text_input(
    "نام روستا:",
    placeholder="مثلاً ده بالا"
)

# -----------------------------
# جستجو
# -----------------------------
if st.button("🔍 جستجوی روستا"):

    if village_name.strip() == "":
        st.warning("لطفاً نام روستا را وارد کنید.")

    else:
        # حذف فاصله‌های اضافی
        search_name = village_name.strip()

        # جستجوی نام روستا
        result = df[
            df["روستا"].astype(str).str.strip() == search_name
        ]

        # -----------------------------
        # اگر روستا پیدا شد
        # -----------------------------
        if not result.empty:

            st.success("روستا پیدا شد.")

            # فقط اولین ردیف
            row = result.iloc[0]

            st.subheader("📋 اطلاعات روستا")

            # نمایش تمام ستون‌های همان ردیف
            for column in df.columns:

                value = row[column]

                # اگر مقدار خالی بود
                if pd.isna(value):
                    value = "اطلاعات ثبت نشده"

                st.write(
                    f"**{column}:** {value}"
                )

        # -----------------------------
        # اگر پیدا نشد
        # -----------------------------
        else:

            st.error(
                f"روستایی با نام «{search_name}» پیدا نشد."
            )

            st.info(
                "لطفاً نام روستا را دقیقاً مطابق فایل Excel وارد کنید."
            )

