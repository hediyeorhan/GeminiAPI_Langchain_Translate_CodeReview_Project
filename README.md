# GeminiAPI_Langchain_Translate_CodeReview_Project

Bu çalışmada Google AI tarafından geliştirilen yapay zekâ Gemini API'ı kullanılarak küçük çaplı bir translate ve code review projesi geliştirilmiştir. 

Projede __.env__ dosyasında içeriğinde şu veriler bulunmaktadır.

• GEMINI_API_KEY=

• LANGCHAIN_API_KEY=

• LANGCHAIN_TRACING_V2=true

• LANGCHAIN_PROJECT=PROJECT_NAME

Projede, Gemini AI ile birlikte Langchain framework'ü kullanılmıştır. Langchain, büyük dil mmodelleri ile uygulama geliştirilmesinde kullanılmaktadır. Output ve input değerlerini isteğimize göre filtrelenmesini, zincir yapısında LLM'lerin birbirleri ile ve insanlar ile konuşmasını sağlamaktadır.

Langchain'in bir hizmeti olan __LangServe__ ile proje deploy edilerek bir arayüz ekranında kullanım kolaylığı sağlamaktadır. Code review projesinin örnek bir çıktısı Şekil 1'de görülmektedir.

<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/96d552b0-9623-43f1-97dd-101fc6214ce0" alt="image">
</div>
Şekil 1. Code review projesinin LangServe kullanılarak gösterimi

<br>
<br>

Langchain'in bir diğer hizmeti __Langsmith__ ile projede arka planda yapılan işlemler, debug işlemleri, ücretli API'ler kullanıldığında ne kadar token kullanıldığı ve kaç dolar harcanıldığı gibi bilgiler bir dashboard üzerinden takip edilebilmektedir. Örnek bir Langsmith ekranı Şekil 2'de görülmektedir.
<br>
<br>

<div align="center">
<img src="https://github.com/user-attachments/assets/3b4b54a8-4a90-4794-9c17-12bb0848756d" alt="image">
</div>

Şekil 2. Örnek Langsmith dashboard ekranı