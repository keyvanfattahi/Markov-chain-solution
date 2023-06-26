# Markov chain solution

The coding of this program is developed with <b><code style="color: red;"> Python </code> </b> and the <b><code style="color: red;"> Streamlit library </code> </b>.

A Markov chain is a random process where the current state depends only on the previous state, meaning that the probability of a new state occurring is only dependent on the current state and not influenced by previous states.

In a Markov chain model, the current state is typically represented by a given state. For example, in a game of chess, the current state would be represented by the position of the pieces on the board and the conditions for moving them. Each new move is predicted by the Markov chain and, due to its dependency on the previous state, is known as a Markov chain.

Markov chains are used in many different applications, including natural language processing, neural networks, economic system analysis, social networks, and more. In some cases, Markov chain models are optimized and improved using statistical algorithms such as the Monte Carlo algorithm.

The mathematical formula for a discrete-time Markov chain is as follows:

<code>P(Xn+1 = j | Xn = i, Xn-1 = i-1, ..., X0 = i0) = P(Xn+1 = j | Xn = i)</code>

This formula represents the probability of transitioning from state i to state j at time n+1, given the current state i at time n, and all previous states up to time 0. The equation simplifies to only depend on the current state, making it a Markov chain.

Here is a visual representation of a simple Markov chain:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Markovkate_01.svg/1200px-Markovkate_01.svg.png" style='width:220px; height:250px'>

Markov Chain Visualization

In this example, there are three states represented by circles: A, B, and C. The arrows represent the probabilities of transitioning from one state to another. For instance, the probability of transitioning from state A to state B is 0.4, and the probability of staying in state A is 0.6.


Developer: Keyvan FattahiRishakan


# حل زنجیره مارکوف

کدنویسی این برنامه با <b><code style="color: red;"> پایتون </code> </b> و <b><code style="color: red;"> کتابخانه Streamlit < توسعه داده شده است. /code> </b>.

زنجیره مارکوف یک فرآیند تصادفی است که در آن حالت فعلی فقط به حالت قبلی بستگی دارد، به این معنی که احتمال وقوع یک حالت جدید فقط به وضعیت فعلی بستگی دارد و تحت تأثیر حالت‌های قبلی نیست.

در مدل زنجیره مارکوف، حالت فعلی معمولاً با یک حالت معین نشان داده می شود. به عنوان مثال، در یک بازی شطرنج، وضعیت فعلی با موقعیت مهره ها روی تخته و شرایط حرکت آنها نشان داده می شود. هر حرکت جدید توسط زنجیره مارکوف پیش بینی می شود و به دلیل وابستگی آن به حالت قبلی، به زنجیره مارکوف معروف است.

زنجیره‌های مارکوف در کاربردهای مختلفی از جمله پردازش زبان طبیعی، شبکه‌های عصبی، تحلیل سیستم‌های اقتصادی، شبکه‌های اجتماعی و غیره استفاده می‌شوند. در برخی موارد، مدل های زنجیره مارکوف با استفاده از الگوریتم های آماری مانند الگوریتم مونت کارلو بهینه و بهبود می یابند.

فرمول ریاضی برای زنجیره مارکوف زمان گسسته به شرح زیر است:

<code>P(Xn+1 = j | Xn = i، Xn-1 = i-1، ...، X0 = i0) = P(Xn+1 = j | Xn = i)</code>

این فرمول نشان دهنده احتمال انتقال از حالت i به حالت j در زمان n+1، با توجه به وضعیت فعلی i در زمان n، و همه حالت های قبلی تا زمان 0 است. یک زنجیر مارکوف

در اینجا یک نمایش تصویری از یک زنجیره مارکوف ساده است:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Markovkate_01.svg/1200px-Markovkate_01.svg.png" style='width:220px; ارتفاع: 250px'>

تجسم زنجیره مارکوف

در این مثال، سه حالت وجود دارد که با دایره‌ها نشان داده می‌شوند: A، B و C. فلش‌ها احتمال انتقال از یک حالت به حالت دیگر را نشان می‌دهند. به عنوان مثال، احتمال انتقال از حالت A به حالت B 0.4 و احتمال ماندن در حالت A 0.6 است.


سازنده: کیوان فتاحی ریشاکان
