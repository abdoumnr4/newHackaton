import google.generativeai as genai

def text_generation(text):

    genai.configure(api_key="AIzaSyBkd78asSHG8EHwrKW66uIEdvZWJhbbZsw")

    # Set up the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                generation_config=generation_config,
                                safety_settings=safety_settings)


    prompt_parts = [
  "input: شنو المشكل الرئيسي اللي خلاك تجي لسبيطار؟",
  "output: خايف يكون عندي جلطة فالقلب.",
  "input: علاش جيتي للطوارئ اليوم؟",
  "output: عندي ألم بزاف فصدري.",
  "input: كيفاش كتحس بالألم اللي عندك؟",
  "output: هو ألم ثقيل كيحزّ فصدري.",
  "input: إمتى بدا الألم؟",
  "output: بدا شي ساعة هادي.",
  "input: واش سبق ليك وحسيتي بشي ألم فصدرك من قبل؟",
  "output: آه، ولكن ما عمرها كانت بهاد الشدة.",
  "input: واش عندك شي أعراض أخرى؟",
  "output: آه، كنحس بضيق فالتنفس وكالغثيان.",
  "input: واش خديتي شي حاجة باش تخفف الألم؟",
  "output: خديت أسبيرين ولكن ما حسيتش بالفرق.",
  "input: واش الألم كيدير فشي بلايص أخرى فالجسم؟",
  "output: آه، كيضرب لي فدراعي اليسر وفي فكي.",
  "input: واش الألم مستمر ولا كيجي ويمشي؟",
  "output: هو مستمر من نهار بدا.",
  "input: واش عندك شي مرض قلبي من قبل؟",
  "output: آه، عندي مرض شرايين القلب.",
  "input: واش كتعرق بزاف ولا حاس براسك بارد؟",
  "output: آه، كنعرق بزاف.",
  "input: واش عندك شي مشكل ديال ضغط الدم؟",
  "output: آه، عندي ارتفاع فضغط الدم من مدة.",
  "input: واش كتدوخ ولا حاس براسك خفيف؟",
  "output: آه، كنحس براسي خفيف بزاف.",
  "input: واش عندك شي عوامل خطورة لأمراض القلب؟",
  "output: آه، عندي السكري وكنت كنكمّي.",
  "input: واش كنتي مضغوط بزاف مؤخرا؟",
  "output: آه، الخدمة كانت مضغوطة بزاف مؤخرا.",
  "input: واش كتقاسي من العيا؟",
  "output: آه، كنحس براسي عيان بزاف هاد الأيام.",
  "input: واش لاحظتي شي نفاخ فريولك ولا كراسك؟",
  "output: لا، ما لاحظتش شي نفاخ.",
  "input: واش كان شي تغييرات فالصحة ولا فالأدوية مؤخرا؟",
  "output: لا، كلشي بحال المعتاد.",
  "input: واش عندك شي تاريخ عائلي مع أمراض القلب؟",
  "output: آه، الوالد ديالي كان عندو جلطة فالقلب فسن 55.",
  "input: واش سبق ليك ودخلتي لسبيطار بسباب ألم فالصدر؟",
  "output: آه، دخلت لسبيطار بسباب جلطة فالقلب من ثلاث سنين.",
  "input: شحال فعمرك؟",
  "output: عندي 50 عام.",
  "input: واش كتكمي؟",
  "output: آه، كنكمي علبة ديال السجائر في النهار.",
  "input: واش كتشد شي دوا على القلب؟",
  "output: آه، كنشد دوا ديال الكوليسترول وضغط الدم.",
  "input: واش شربتي شي حاجة اليوم؟",
  "output: غير الما والقهوة.",
  "input: واش كتاكل مزيان؟",
  "output: عادي، ما عنديش شي شهية كبيرة.",
  "input: واش كتدير شي رياضة؟",
  "output: كنمشي غير شوية.",
  "input: واش كتسوق بزاف؟",
  "output: آه، الخدمة ديالي كتطلب مني نسوق بزاف.",
  "input: واش عندك شي ضربة ولا شي جرح فالصدر؟",
  "output: لا، ما عندي والو.",
  "input: واش كنتي مريض شي مرة بزكام ولا أنفلونزا؟",
  "output: آه، كنت مريض بواحد الزكام الشهر اللي فات.",
  "input: واش كتنعس مزيان بالليل؟",
  "output: لا، كنفيق بزاف بالليل.",
  "input: واش عندك شي مشاكل فالهضم؟",
  "output: آه، مرات كنحس بالحرقان.",
  "input: واش عندك شي سكر فالعائلة؟",
  "output: آه، عندنا السكر فالعائلة.",
  "input: واش كتاخد شي مكملات غذائية؟",
  "output: آه، كنشد فيتامينات.",
  "input: واش عندك شي أمراض مزمنة أخرى؟",
  "output: لا، غير مشاكل القلب.",
  "input: واش كتجيك حالات ديال الغثيان من غير اليوم؟",
  "output: آه، مرات كيجيوني.",
  "input: واش كتاكل أكلات مالحة بزاف؟",
  "output: آه، كنحب المالح بزاف.",
  "input: واش كتشرب الكحول؟",
  "output: مرات كنشرب شي كاس.",
  "input: واش كتلاحظ شي تغير فوزنك؟",
  "output: آه، زدت شي كيلوين هاد الشهر.",
  "input: واش كتحس براسك مقلق بزاف؟",
  "output: آه، كنقلق بزاف هاد الأيام.",
  "input: واش كتشد شي دوا للقلق؟",
  "output: لا، ما كنشد والو.",
  "input: واش عندك شي مشاكل مع النوم؟",
  "output: آه، كنحس براسي ما كنفيقش ناشط.",
  "input: واش كتحس براسك ضعيف؟",
  "output: آه، مرات كنحس بضعف.",
  "input: واش عندك شي صداع مستمر؟",
  "output: آه، مرات كيجيوني الصداع.",
  "input: واش كتحس بشي تنمل فإيديك ولا رجليك؟",
  "output: آه، مرات كنحس بتنمل.",
  "input: واش كتحس بضربة قلبك سريعة؟",
  "output: آه، مرات كتحس ضربات القلب بزاف.",
  "input: واش كتلاحظ شي تقلبات فالمود ديالك؟",
  "output: آه، مرات كنكون فرحان ومرات مقلق."
]

    text = ["input:"+text, "output: ",]
    prompt_parts.extend(text)

    response = model.generate_content(prompt_parts)
    return response.text