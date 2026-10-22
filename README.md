# Sıcaklık İzleyici ROS 2 Paketi

Bu paket, rastgele sıcaklık verisi üreten bir sensör düğümü ve bu veriyi okuyup eşik değerine göre uyarı veren bir izleyici düğümü içerir.

## Derleme ve Çalıştırma Adımları
1. Paketi derlemek için ana çalışma alanında şu komutu çalıştırın:
   `colcon build --packages-select sicaklik_izleyici_py`
2. Ortamı kaynaklayın:
   `source install/setup.bash`
3. Birinci terminalde sensör düğümünü başlatın:
   `ros2 run sicaklik_izleyici_py sensor`
4. İkinci terminalde izleyici düğümünü başlatın:
   `ros2 run sicaklik_izleyici_py izleyici`
