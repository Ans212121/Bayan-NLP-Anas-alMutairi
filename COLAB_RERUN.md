# إعادة التشغيل في Colab

هذه تعديلات جاهزة للتشغيل، وليست نتائج جديدة. افتح الدفاتر من جدول README واحفظ نسخة في Drive. احفظها بعد التشغيل مع المخرجات، ولا تعتمد ظهور نتائج تاريخية قبل اختيار Restart session and run all.

1. اسم المستودع المطلوب هو `bayan-nlp-Ans212121`. أداة GitHub المتاحة لا تتضمن إعادة التسمية. من Settings > General غيّر الاسم إذا أردت إغلاق هذا الجزء من A1، ثم حدّث روابط README وPROJECT_SUMMARY وSUBMISSION ومتغير REPO_URL في الدفاتر بالاسم الجديد قبل التشغيل.
2. شغّل 00 ثم 01 ثم 02 في جلسة نظيفة لكل دفتر. خلية البداية تستنسخ المستودع للقراءة وتطبع RUN_COMMIT. لا تنفذ دفعًا إلى GitHub. إذا سبق فتح جلسة قديمة، احذف جلسة Colab من القائمة وابدأ جلسة جديدة حتى لا تعمل على نسخة قديمة.
3. افتح 03 واختر GPU إن توفر، ثم Run all. التدريب يختار أفضل epoch على validation، ويقارن الموضوع والمشاعر كلًا بخط أساس مستقل. وافق على ربط Drive حين يطلب Colab ذلك. لا تغيّر الإعدادات بناءً على test؛ نتائج test القديمة كانت منشورة أصلًا.
4. تأكد من وجود `MyDrive/bayan-correction/topic-model` و`sentiment-model` و`topic_validation.csv` و`topic_validation_predictions.json` و`topic_contract.json`. احتفظ بالأوزان في Drive ولا ترفعها إلى GitHub. التقارير الصغيرة في مجلد reports في Drive.
5. شغّل 04 ثم 05 ثم 06 في جلسات مستقلة واحفظ المخرجات. شغّل 07؛ جزؤه الأول مثال COURSE_FIXTURE، وجزء التصحيح الأخير يستخدم تنبؤات نموذجك من 03 ويكتب project_evaluation.json وproject_slice_report.csv. املأ `project_error_review.csv` في Drive بتصنيف الأخطاء وأسبابها وإصلاحاتها بعد قراءتها. لا تغيّر النص/الحقيقة/التنبؤ في الجدول. أعد الجزء الأخير بعد المراجعة. إذا لم توجد أخطاء، اكتب ذلك ولا تنسب أخطاء المثال الجاهز لنموذجك؛ يلزم مجموعة validation مستقلة مسموحة لتحليل أوسع، وليس فتح test للتحسين.
6. افتح 08 في جلسة CPU جديدة. اترك PROJECT_MODE=True. بعد ربط Drive، راجع ميزانية TARGET قبل القياس، وعدّلها بما تستطيع تبريره ثم اجعل BUDGET_CONFIRMED=True. القيم المقترحة ليست نتائج ولا إثباتًا لاجتياز الأهداف الرسمية. أكمل التشغيل؛ سيقارن PyTorch وONNX وINT8 على نموذج الموضوع الفعلي وبيانات validation ثم يختبر الخدمة وbatch endpoint. انتظر 30 تكرارًا لكل مقارنة؛ لا تنقل نتائج smoke القديمة لهذا التشغيل.
7. احفظ الدفاتر بأسمائها التسعة ومخرجاتها، واجمع التقارير الصغيرة من Drive: observed_classification.json، observed_sentiment.json، project_tokenizer.json، project_evaluation.json، project_slice_report.csv، project_error_review.csv، benchmark_results.json، service_smoke.json، extension_batch_endpoint.json. أرسل الملفات هنا ليجري التحقق منها وتحديث المستودع عبر GitHub connector؛ لا يكفي أن تقول Run all نجح.
8. بعد دمج المخرجات الحقيقية، شغّل فاحص الدورة من جذر النسخة في Colab:

```python
import subprocess, sys, os
subprocess.run([sys.executable, "-m", "pytest", "-q", "tests"], check=True)
subprocess.run([sys.executable, "scripts/validate_submission.py", ".", "--json-report", "reports/submission_validation.json"])
subprocess.run([sys.executable, "scripts/preflight_submission.py", ".", "--report", "reports/preflight.json"])
```

نتيجة FAIL الحالية متوقعة بسبب خلايا جديدة غير منفذة وأدلة معلقة؛ لا تغيّر الفاحص لتجاوزها. لا تحوّل tests_passed أو benchmark_mode إلى قيمة النجاح إلا بعد التحقق. لا تنشئ tag الآن. بعد اكتمال الأدلة ومراجعة الإقرار تطلب أنت صراحة تثبيت النسخة النهائية. سياسة الدورة تقيم SHA المستلم مرة واحدة؛ هذه التعديلات لا تضمن قبول إعادة التصحيح.

التصحيح محفوظ في فرع `correction-evidence-audit-20260930` بسبب التعديل المتزامن على main. روابط README وخلية الاستنساخ تستخدم هذا الفرع. بعد الدمج حدّث الاثنين معًا إلى main. فاحص الروابط الرسمي يتوقع main، لذا سيشير مؤقتًا إلى روابط الفرع كعائق حتى الدمج.

Sentiment split audit: train negative/positive/neutral = 10/8/6; validation negative/neutral = 2/6 (no positive); test positive/negative = 2/6 (no neutral). Preserve the supplied grouped split, report fixed-contract Macro-F1 and support, and do not claim representative three-class performance.
