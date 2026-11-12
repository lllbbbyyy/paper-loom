# Behavioral cases / 行为评估用例

These cases are reusable review prompts, not a claim of measured model performance. Give a future evaluator the request, the skill, and the input. Judge the resulting artifacts against the observable criteria. Do not supply the expected rewritten wording.

这些是可复用的评估请求，不代表已测得的模型性能。后续评价时提供请求、skill 和输入，按可观察标准检查产物，不预先提供标准改写句。

## A. Missing bridge / 缺失的逻辑桥梁

Request: revise and annotate this introduction paragraph only.

Input: “Hardware configurations are numerous. Neural networks fit nonlinear functions. Therefore, we build a component graph.”

Pass: identifies the missing reason for decomposition, distinguishes a proposed premise from supplied evidence, and creates local paragraph/sentence records. It does not claim that adding “therefore” solves the gap.

请求：只修改并标注这一引言段落。通过标准：定位分解动机缺失，区分拟议前提与已有证据，建立局部段落和句子卡，不把添加连接词当作解决方法。

## B. Full miniature paper / 完整微型稿件

Request: use the skill on `skills/paper-loom/examples/en/manuscript.md` or its Chinese equivalent and maintain per-unit documents.

Pass: includes the abstract and all other sections, separate files for sections, paragraphs, and sentences, explicit reading order, exact source wording, and contextual incoming/outgoing links. The evaluation remains planned, not reported as a success.

通过标准：覆盖摘要与其他章节，逐层独立文件、明确顺序、原句一致、具体承接关系；计划评价不能写成已经成功。

## C. Mixed classification / 分类维度混杂

Input outline: “Related work: neural methods, robotics papers, recent systems. Challenges: speed, a controller, a data module.”

Pass: identifies the mixed classification axes and the difference between a challenge and a module name. Proposes a relevant common axis without claiming it exhausts the field. Does not invent literature or force three matched challenges.

通过标准：指出分类维度混杂、挑战与模块命名混淆，提出有任务依据的共同维度，不宣称穷尽领域，不编造文献或硬凑三项对应。

## D. Limited abstract budget / 摘要压缩

Request: shorten an abstract to the user’s word budget while preserving motivation, the mechanism, and supplied numerical facts.

Pass: removes low-level inventories before the causal link between need and method. Keeps metric denominators, comparison scope, and unsupported results marked as unavailable. Does not introduce a default venue-specific word limit.

通过标准：先压缩细节，保留需求到方法的关系、指标参照和主张范围，不自设某个会议的统一字数要求。

## E. Evidence mismatch / 证据不支持主张

Input: “Average error is lower on two tasks. Therefore, the method guarantees reliable prediction for every component.”

Pass: narrows the universal claim to the actual observations and identifies the missing per-component evidence. Does not fabricate tests, suppress the weaker result, or launch experiments without authorization.

通过标准：收窄全称结论，明确缺少逐组件证据，不编造、不隐藏、不自行开展实验。

## F. Mutation after annotation / 修改后的同步

Request: merge two sentences, move a paragraph, and revise the main claim after new evidence.

Pass: updates exact sentences, parent lists, reciprocal neighbor links, and affected abstract/conclusion claims. Retains stable IDs where possible and retires deleted ones. No stale records remain presented as current.

通过标准：更新原句、上层清单、前后邻居及受影响的摘要结论，维护稳定 ID，删除失效关联，不保留伪装成当前版本的旧标注。

## G. English punctuation / 英文标点

Input includes “white-box model,” an invented six-part hyphenated adjective, a semicolon chain, and a mathematical minus sign.

Pass: retains standard terminology and mathematical notation, decomposes competing assertions, and does not apply a blanket ban on punctuation.

通过标准：保留规范术语和数学符号，拆开竞争重点，不机械禁止所有连字符、分号或破折号。

## H. Local scope and translation / 局部范围与翻译

Request: translate and improve one sentence only, using two target-language sentences if clearer.

Pass: preserves meaning and evidence strength, keeps work local, records one-to-many mapping, and checks neighboring transitions without rewriting the whole manuscript.

通过标准：保留意义和证据强度，允许一对多映射，检查相邻衔接，不扩展为整篇重写。

## Assessment / 评价方法

Assess evidence fidelity, argument alignment, concrete transitions, scope discipline, annotation coverage, synchronization, and readability separately. A missing fact must not be hidden by a high fluency score. Check the clean prose as well as the records: convincing annotations cannot compensate for a disconnected manuscript.

分别评价事实保持、论证对应、具体衔接、范围控制、标注覆盖、同步和可读性。流畅度不能掩盖证据缺失；标注写得漂亮也不能替代正文连贯。
