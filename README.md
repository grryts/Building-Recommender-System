# Building-Recommender-System
create a recommendation system using Python, the data used here is the film database from imdb complete with its metadata


Analisis yang telah dilakukan melalui kode tersebut memberikan wawasan yang berharga dalam memahami data film dan rating. Kita memulai dengan membersihkan data, menghilangkan entri yang memiliki nilai NULL pada kolom penting seperti judul utama, judul asli, dan genre. Hal ini penting agar data yang kita gunakan dalam analisis memiliki kualitas yang baik.

Selanjutnya, kita menggabungkan tabel film dan tabel rating. Dengan melakukan penggabungan ini, kita dapat melihat bagaimana rating film berhubungan dengan atribut-atribut lainnya, seperti judul, genre, tahun rilis, dan durasi film. Ini membuka peluang untuk membangun sistem rekomendasi yang lebih akurat dan personal.

Selanjutnya, kita membangun sistem rekomendasi sederhana berdasarkan perhitungan nilai rata-rata rating (C) dan jumlah suara (m). Nilai C merupakan rata-rata rating dari seluruh film, sementara nilai m digunakan sebagai ambang batas jumlah suara agar film yang diikutsertakan dalam rekomendasi memiliki tingkat popularitas yang signifikan. Dengan sistem ini, kita dapat menghasilkan daftar film yang direkomendasikan berdasarkan peringkat tertinggi.

Namun, kita juga memberikan pengguna kemampuan untuk mengatur preferensi mereka sendiri. Dalam fitur "User Preference Recommender", pengguna dapat memilih apakah ingin film yang hanya untuk dewasa atau tidak, tahun rilis film, dan genre film yang diminati. Sistem akan memberikan rekomendasi film yang sesuai dengan preferensi tersebut, memungkinkan pengguna untuk menemukan film-film menarik yang sesuai dengan minat dan preferensi mereka.

Dalam kesimpulannya, analisis ini memberikan gambaran tentang bagaimana data film dan rating dapat digunakan untuk membangun sistem rekomendasi yang akurat dan personal. Dengan sistem ini, pengguna dapat menemukan film-film yang menarik berdasarkan peringkat tertinggi dan juga sesuai dengan preferensi mereka. Analisis ini memberikan wawasan berharga dalam memahami dan memanfaatkan data untuk memberikan pengalaman menonton film yang lebih baik dan memuaskan.
