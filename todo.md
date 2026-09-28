# Lista zadań do poprawy artykułu (ECOINF-D-26-00015 - Major Revision)

### Kod, Dane i Wymogi Formalne
- [ ] [ ] #4 Utworzyć publiczne, posprzątane repozytorium z kodem i zbiorem danych
- [ ] [ ] #4 Dodać sekcję "Data Availability" przed bibliografią, w której będzie link/DOI do repozytorium.
- [ ] [X] #4 Wstęp ma zły format - powinien bardziej się skupiać na powiazanych pracach, lukach, motywacji, celach i wkładzie, a mniej na opisach owoców (to do sekcji 3)
- [ ] [X] #4 Podkreślić nowotorski charakter pracy (rozwój zbioru danych, ocena sprzętu i metodologia wraz z porównaniem do innych prac)
- [ ] [X] #1 4 Dodać dlaczego wprowadzenie naszego zbioru jest wartościowe (poza nakładaniem się klas)
- [ ] [ ] #4 Opis topologii jest niespójny. W 5.1. opisywany jest jako liniowy a na rys. 6 i dyskusja dotycząca braku łańcucha czterokubitowego sugerują coś innego
- [ ] [ ] #4 Uporządkować i ujednolicić strukturę, zbierając rozproszone informacje metodyczne (obecnie w sekcjach 4 i 5.2). Zastosować nowy, wyraźny podział na sekcje: Introduction, Literature Review, Dataset Description, Methodology, Experimental Setup, Results, Discussion/Limitations oraz Conclusion.
- [ ] [X] #4 Wyraźniej uzasadnić znaczenie pracy w kontekście ekologii, rolnictwa i bioróżnorodności - praca wygląda głównie jak benchmark QML – należy dobitniej pokazać, dlaczego klasyfikacja tych konkretnych roślin jest ważna i potrzebna z praktycznego punktu widzenia.
- [ ] [ ] #3 Dodać krótkie oświadczenie dotyczące praw własności i etyki wykorzystania certyfikowanego materiału roślinnego. - z tego co wyczytałem to trzeba opisać w ramach oświadczenia/sekcji "Ethics Statement": 
- źródło pochodzenia 
- zgoda na badania
- deklaracja, że wykorzystanie tych roślin nie narusza praw autorstkich ani "praw wyłącznych hodowców odmian"
- oświadczenie, że dane udostępniamy publicznie w celach *NAUKOWYCH - NIE KOMERCYJNYCH*
- dałbym to za wnioskami przed bibliografią
- powtarzające się informacje bym względnie zostawił, ewentualnie bym skracał jezeli jest jakiś limit
np. 

**Ethics Statement**
The plant material (Cornus mas L. cultivars) used to generate the dataset was sourced from the Arboretum and Institute of Physiography in Bolestraszyce, Poland. The morphological measurements were conducted with the permission of the Institute's head, N. Piórecki. We declare that the collection of this data complied with institutional practices, and the public release of this dataset for non-commercial, scientific research purposes does not infringe upon any existing plant breeders' rights or intellectual property ownership.

### Analiza Zbioru Danych i Statystyki
- [ ] [X] #3 4 Uzupełnić tekst o liczbę próbek dla każdej z klas i podziałów (treningowy, walidacyjny, testowy) i ogólnie opisać współczynnik podziału czy walidacji krzyżowej.
- [ ] [X] #1 2 Dodać szczegółowe statystyki opisowe dla cech i odmian: średnie, odchylenia standardowe, macierze separowalności, wizualizacja granic decyzyjnych, formalne testy normalności rozkładu i separowalności (np. ANOVA lub MANOVA).
- [ ] [X] #2 Uzasadnić czemu masy nie zostały uwzględnione (poza wzmianką o różnych porach zbioru)
- [ ] [X] #2 Opisać ryzyko związane z małą liczbą próbek 
- [ ] [X] #4 Opisać dokładniej wstępne przetwarzanie danych (metody normalizacji, zakres skalowania)
- [ ] [X] #R Rozbudować opis zbioru na dwie sekcje 1) Opis zbioru z motywacją (to co kazali z intro przenieśc) 2) analiza statystyczna i porównanie wyników na klasykach i irysach
- [ ] [X] Zrobić testy statystyczne potwierdzające trudność zbioru oraz separowalność klas.
- [ ] [X] #3 "The data were collected between 2007 and 2012, but potential batch effects across different harvest years are not discussed" ? 
- [ ] [X] #3 Opisać dlaczego wybrano akurat te odmiany (czy mają znaczenie ekonomiczne lub są różne morfologicznie)
- [ ] [ ] #4 Dopisać jaka cecha została usunięta i w jaki sposób została wybrana.
- [ ] [X] #4 Wyjaśnić, czy obserwacje i pomiary pochodzą z tych samych drzew, zbiorów czy lat, oraz wziąć pod uwagę potencjalne zależności między nimi podczas dzielenia danych na zbiory treningowe i testowe .
- [ ] [X] #2 Usunąć stałe ziarno losowości, przeprowadzić testy i uśrednić wyniki, aby udowodnić stabilność modelu. (nie usuwać ziarna tylko przeprowadzić testy dla różnych ziaren)

### Metodologia i Klasyczne Modele Bazowe (Baseline)
- [ ] [ ] #3 4 Uzupełnić tekst o podział (treningowy, walidacyjny, testowy) i ogólnie opisać współczynnik podziału czy walidacji krzyżowej - tu bym napisał, że jest jak w przypadku ewaluacji metod klasycznych sec:3
- [ ] [ ] #1 4 Dodać klasyczne modele uczenia maszynowego (np. SVM, Random Forest, K-NN) dla porównania i sugestia by dodać jeszcze jedną metodę kwantową (ja bym dodał jedynie nowy ansatz, QSVM będzie znacznie lepszy więc bez sensu) - to w opisie zbioru, tam umieścić i przedstawic, że jest trudniejszy od Iris (porównanie IRIS vs derenie).
- [ ] [ ] #2 4 Dodać informację o hiperparametrach uczenia: wielkość batcha, learning rate, liczbę epok, funkcję straty i metodę optymalizacji - z naciskiem na implementowany optymalizator dla łatwiejszej replikacji.
- [ ] [ ] #2 Usunąć stałe ziarno losowości, przeprowadzić testy i uśrednić wyniki, aby udowodnić stabilność modelu. (nie usuwać ziarna tylko przeprowadzić testy dla różnych ziaren)
- [ ] [ ] #4 *The multiclass classification mechanism is not sufficiently explained. Cornus is a five-class problem and Iris is a three-class problem, yet the mapping between quantum measurement outputs and class labels is not described. The keyword "binary classification" is also inconsistent with the reported experiments.*?
- [ ] [ ] #4 Opisać dokładniej wstępne przetwarzanie danych (metody normalizacji, zakres skalowania)
- [ ] [ ] #4 Doprecyzować opis "fully quantum" - zarzut, że to klasyk - optymalizacja na klasyku i wstępne przetwarzanie
- [ ] [ ] #4 Dodać 5 - cechowy zbiór danych - bo jest uwzględniony w opisach - lub napisać czemu nie został uwzględniony
- [ ] [ ] #4 Brak podstawowych informacji o rzeczywistym układzie (liczba shotów, powtórzeń, mapowanie kubitów, ustawienia transpilacji, głębokość obwodu?(to chyba było analizowane), liczba bramek dwukubitowych, liczba operacji SWAP, informacje o kalibracji, opis procedur minimalizacji błędów).

### Przegląd literatury
- [ ] [X] #2 Poszerzyć o dyskusje nt: 
- [ ] [X] jałowych płaskowyży
- [ ] [X] metod redukcji szumów
- [ ] [X] podejść hybrydowych
- [ ] [X]porównać się z metodami hybrydowymi
- [ ] [X] #2 Wzmocnić motywacje - dlaczego sensowne jest podejście kwantowe w tym konkretnym zadaniu w porównaniu z klasykami - sugestia odwołania się do doi: 10.1007/s43674-023-00054-2; 10.1080/03610918.2024.2330700
- Jezeli ktoś coś wymyśli to dodac jak nie to odbić

*in this regard, Enhance connections to recent literature that demonstrates the great potential and use of neural network (doi: 10.1007/s43674-023-00054-2; 10.1080/03610918.2024.2330700) for modelling complicated (nonlinear) patterns across a broad variety of study subjects in order to further motivate the exploration of neural network models in your present work, since situating the quantum neural network within the broader neural network paradigm would help readers appreciate both the continuity and the departure that QNNs represent relative to classical architectures.*


### Eksperymenty Kwantowe, Wyniki i Korekta
- [ ] [ ] #1 Dodać lepszą analizę dlaczego na 4 cechach jest gorzej. (Szumy, głębokość obwodów, kodowanie danych, architektura).
- [ ] [ ] #4 Nie pisać, że architektura QNN jest nowatorska wg recenzenta nie jest a jeżeli jest to dosadniej udownodnić (pomysł nie ale realhardware implementacja tak)
- [ ] [ ] #2 #4 Rozbudować sekcję wyników: dodać macierze pomyłek, metryki oraz przedziały ufności/odchylenia na wykresach.
- [ ] [ ] #4 Przeorganizować strukturę artykułu, opisać topologię sprzętu, czasy wykonania, poprawić błędy językowe i usunąć niepotrzebne dygresje (np. wątek o żelkach).
- [ ] [ ] #2 Wytłumaczyć anomalię z 25 warstwami dla irysów i 4 cechami dlaczego spada poniżej 50% (jest to za mało opisane)
- [ ] [ ] #3 Bardziej konkretnie opisać future works.
- [ ] [ ] #4 Wniosek, że zwiększanie głębokości obwodów zmniejsza dokładność głównie z powodu szumu kwantowego, jest niewystarczająco udowodniony. Porównanie symulacji bezszumowej, symulacji z szumem i rzeczywistego sprzętu, wraz z analizami głębokości obwodów i liczby bramek, lepiej to uzasadni.
- [ ] [ ]#4 Tabela 2 i dyskusja opisują selektywne powtórzenia i podają wynik sprzętowy 65,5%, który nie jest jasno przedstawiony w tabeli. Poprawić spójność i przejrzystość

**Spotkanie**
- [X] [X] zmienić seed na stone (ziarno na pestkę)
- [X] [X] znormalizować wyniki testów
- [ ] [ ] zobaczyć jaka cecha była usunięta w pierwotnych badaniach i rozważyć usunięcie najmniej istotnych - nie ma tego :P 

**Podział**
- [ ] [ ] Nowe eksperymenty kwantowe - Radek
- [ ] [ ] Redakcja artykułu, testy statystyczne, testy klasyków - Konrad
- [ ] [ ] Konsultacje części przyrodniczych i dodatkowe informacje - Mateusz

**Prośba o dodatkowe informacje**
- [ ] [X] #4 Wyraźniej uzasadnić znaczenie pracy w kontekście ekologii, rolnictwa i bioróżnorodności - praca wygląda głównie jak benchmark QML – należy dobitniej pokazać, dlaczego klasyfikacja tych konkretnych roślin jest ważna i potrzebna z praktycznego punktu widzenia.
- [ ] [ ] #4 Przejrzeć i poprawić *"ethic statement"*
- [ ] [X] #4 Uzasadnić czemu masy nie zostały uwzględnione (poza wzmianką o różnych porach zbioru)]
- [ ] [X] #1 4 Dodać dlaczego wprowadzenie naszego zbioru jest wartościowe (poza nakładaniem się klas)
- [ ] [X] #2 Opisać ryzyko związane z małą liczbą próbek
- [ ] [X] #3 "The data were collected between 2007 and 2012, but potential batch effects across different harvest years are not discussed"
- [ ] [X] #3 Opisać dlaczego wybrano akurat te odmiany (czy mają znaczenie ekonomiczne lub są różne morfologicznie)
- [ ] [ ] #4 Dopisać jaka cecha została usunięta i w jaki sposób została wybrana. (mało istotna statystycznie i było ich mniej 350vs450 próbek)
- [ ] [X] #4 Wyjaśnić, czy obserwacje i pomiary pochodzą z tych samych drzew, zbiorów czy lat, oraz wziąć pod uwagę potencjalne zależności między nimi podczas dzielenia danych na zbiory treningowe i testowe .
- [ ] [ ] #4 *The multiclass classification mechanism is not sufficiently explained. Cornus is a five-class problem and Iris is a three-class problem, yet the mapping between quantum measurement outputs and class labels is not described. The keyword "binary classification" is also inconsistent with the reported experiments.*?
- [ ] [ ] #4 Doprecyzować opis "fully quantum" - zarzut, że to klasyk - optymalizacja na klasyku i wstępne przetwarzanie (usunąć fully quantum, ja bym dopisał, że ostateczną decyzje podejmują kwanty)