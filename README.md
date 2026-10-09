# Image Fusion Review | 图像融合论文与代码

图像融合论文与开源代码整理，涵盖红外与可见光、医学图像、多聚焦、多曝光、遥感和视频融合。按应用任务分类，并标注配准、任务驱动、扩散模型、文本控制等研究方向，方便查找论文和实现。

A collection of image fusion papers and code: infrared and visible image fusion, multimodal medical image fusion, multi-focus fusion, multi-exposure fusion, remote sensing, and video fusion.

**74 篇论文 · 更新于 2026-10-09**

按下方任务目录查找论文与代码，数据集索引见文末。

可使用 GitHub 页面搜索（Ctrl+F）查找方法、年份或关键词。

## 目录

| 任务 | 论文数 | 入口 |
| :-- | --: | :-- |
| 红外与可见光 | 48 | [查看](#ivif) |
| 医学图像 | 15 | [查看](#medical) |
| 通用融合 | 21 | [查看](#general) |
| 多聚焦 | 7 | [查看](#focus) |
| 多曝光 | 7 | [查看](#exposure) |
| 遥感与高光谱 | 1 | [查看](#remote) |
| 视频融合 | 1 | [查看](#video) |
| 融合质量评价 | 2 | [查看](#assessment) |
| 相关工作（非双源像素融合） | 2 | [查看](#related) |

各表按年份倒序排列。同一方法涉及多个任务时，会出现在对应表中。

<a id="ivif"></a>
## 红外与可见光

| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题 | 论文 / 代码 |
| :-- | :-- | :-- | :-- | :-- |
| **APTP / UPTP** | 2026 · CVPR | Beyond Strict Pairing: Arbitrarily Paired Training for High-Performance Infrared and Visible Image Fusion | 非配对训练 / 数据效率 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Deng_Beyond_Strict_Pairing_Arbitrarily_Paired_Training_for_High-Performance_Infrared_and_CVPR_2026_paper.html) · — |
| **CLDyN** | 2026 · CVPR | Customized Fusion: A Closed-Loop Dynamic Network for Adaptive Multi-Task-Aware Infrared-Visible Image Fusion | 任务驱动 / 闭环反馈 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_Customized_Fusion_A_Closed-Loop_Dynamic_Network_for_Adaptive_Multi-Task-Aware_Infrared-Visible_CVPR_2026_paper.html) · [Code](https://github.com/YR0211/CLDyN) |
| **DPOFusion** | 2026 · CVPR | Fusion in Your Way: Aligning Image Fusion with Heterogeneous Demands via Direct Preference Optimization | 偏好优化 / 可控融合 | [Paper](https://arxiv.org/abs/2605.06049) · [Code](https://github.com/suweijian1996/DPOFusion) |
| **DSPFusion** | 2026 · TIP | DSPFusion: Image Fusion via Degradation and Semantic Dual-Prior Guidance | 语义先验 / 退化鲁棒 | [Paper](https://doi.org/10.1109/TIP.2026.3700938) · [Code](https://github.com/Linfeng-Tang/DSPFusion) |
| **EVAFusion** | 2026 · CVPR | Bridging Human Evaluation to Infrared and Visible Image Fusion | 人类评价 / 奖励学习 | [Paper](https://arxiv.org/abs/2603.03871) · [Code](https://github.com/ALKA-Wind/EVAFusion) |
| **FusionRegister** | 2026 · CVPR | FusionRegister: Every Infrared and Visible Image Fusion Deserves Registration | 配准 | [Paper](https://arxiv.org/abs/2603.07667) · [Code](https://github.com/bociic/FusionRegister) |
| **GrFormer** | 2026 · Information Fusion | GrFormer: A Novel Transformer on Grassmann Manifold for Infrared and Visible Image Fusion | Transformer | [Paper](https://www.sciencedirect.com/science/article/pii/S1566253525004750?via%3Dihub) · [Code](https://github.com/Shaoyun2023/GrFormer) |
| **Mask-DiFuser** | 2026 · TPAMI | Mask-DiFuser: A Masked Diffusion Model for Unified Unsupervised Image Fusion | 扩散 | [Paper](https://ieeexplore.ieee.org/document/11162636) · [Code](https://github.com/Linfeng-Tang/Mask-DiFuser) |
| **MobileFusion** | 2026 · ICML | MobileFusion: Mobile-Friendly Infrared and Visible Image Fusion via Structural Re-parameterization | 结构重参数化 / 轻量化 | [Paper](https://proceedings.mlr.press/v306/duan26a.html) · [Code](https://github.com/sucessfullys/MobileFusion) |
| **ReCoFuse** | 2026 · CVPR | ReCoFuse: Ultra-Robust Image Fusion via Restorative Multi-Modal Diffusion Reciprocal Coupling | 扩散 / 退化鲁棒 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_ReCoFuse_Ultra-Robust_Image_Fusion_via_Restorative_Multi-Modal_Diffusion_Reciprocal_Coupling_CVPR_2026_paper.html) · [Code](https://github.com/HaoZhang1018/ReCoFuse) |
| **RegionFuse** | 2026 · CVPR | RegionFuse: Region-Adaptive Pixel Distribution Learning for Infrared and Visible Image Fusion | 区域自适应 / 分布学习 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xia_RegionFuse_Region-Adaptive_Pixel_Distribution_Learning_for_Infrared_and_Visible_Image_CVPR_2026_paper.html) · [Code](https://github.com/DarkIceField/RegionFuse)（代码待发布） |
| **TEDFusion** | 2026 · ICML | Text-Driven Fusion for Infrared and Visible Images: Achieving Image Scene Adaptation on Hyperbolic Space | 文本训练先验 / 双曲空间 | [Paper](https://proceedings.mlr.press/v306/kang26k.html) · [Code](https://github.com/Shaoyun2023/TEDFusion) |
| **C2RF** | 2025 · IJCV | C2RF: Bridging Multi-modal Image Registration and Fusion via Commonality Mining and Contrastive Learning | 配准 | [Paper](https://doi.org/10.1007/s11263-025-02427-1) · [Code](https://github.com/QinglongYan-hub/C2RF) |
| **ControlFusion** | 2025 · NeurIPS | ControlFusion: A Controllable Image Fusion Framework with Language-Vision Degradation Prompts | 文本引导 / 可控融合 / 退化鲁棒 | [Paper](https://arxiv.org/abs/2503.23356) · [Code](https://github.com/Linfeng-Tang/ControlFusion) |
| **DCEvo** | 2025 · CVPR | DCEvo: Discriminative Cross-dimensional Evolutionary Learning for Infrared and Visible Image Fusion | 任务驱动 | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_DCEvo_Discriminative_Cross-Dimensional_Evolutionary_Learning_for_Infrared_and_Visible_Image_CVPR_2025_paper.html) · [Code](https://github.com/Beate-Suy-Zhang/DCEvo) |
| **Deno-IF** | 2025 · NeurIPS | Deno-IF: Unsupervised noisy visible and infrared image fusion method | 退化鲁棒 / 去噪 | [Paper](https://openreview.net/pdf?id=36cKp4tsHF) · [Code](https://github.com/hanna-xu/Deno-IF) |
| **GIFNet** | 2025 · CVPR | One Model for ALL: Low-Level Task Interaction Is a Key to Task-Agnostic Image Fusion | 通用融合 / 联合训练 | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Cheng_One_Model_for_ALL_Low-Level_Task_Interaction_Is_a_Key_CVPR_2025_paper.html) · [Code](https://github.com/AWCXV/GIFNet) |
| **IDF-TDDT** | 2025 · Information Fusion | Instruction-Driven Fusion of Infrared-Visible Images: Tailoring for Diverse Downstream Tasks | 任务驱动 / 指令引导 | [Paper](https://www.sciencedirect.com/science/article/pii/S1566253525002210) · [Code](https://github.com/YR0211/IDF-TDDT) |
| **LUT-Fuse** | 2025 · ICCV | LUT-Fuse: Towards Extremely Fast Infrared and Visible Image Fusion via Distillation to Learnable Look-Up Tables | 蒸馏 / LUT / 轻量化 | [Paper](https://arxiv.org/pdf/2509.00346) · [Code](https://github.com/zyb5/LUT-Fuse) |
| **MaeFuse** | 2025 · TIP | MaeFuse: Transferring Omni Features with Pretrained Masked Autoencoders for Infrared and Visible Image Fusion via Guided Training | 语义先验 | [Paper](https://arxiv.org/abs/2404.11016) · [Code](https://github.com/Henry-Lee-real/MaeFuse) |
| **MAFS** | 2025 · TIP | MAFS: Masked Autoencoder for Infrared-VisibleImage Fusion and Semantic Segmentation | 任务驱动 | [Paper](https://arxiv.org/pdf/2509.11817) · [Code](https://github.com/Abraham-Einstein/MAFS) |
| **MMAE** | 2025 · Pattern Recognition | MMAE: A universal image fusion method via mask attention mechanism | 通用融合 | [Paper](https://doi.org/10.1016/j.patcog.2024.111041) · [Code](https://github.com/xiangxiang-wang/MMAE) |
| **MulFS-CAP** | 2025 · TPAMI | MulFS-CAP: Multimodal Fusion-Supervised Cross-Modality Alignment Perception for Unregistered Infrared-Visible Image Fusion | 配准 | [Paper](https://ieeexplore.ieee.org/abstract/document/10856402) · [Code](https://github.com/YR0211/MulFS-CAP) |
| **OCCO** | 2025 · IJCV | OCCO: LVM-guided Infrared and Visible Image Fusion Framework based on Object-aware and Contextual COntrastive Learning | 语义先验 | [Paper](https://link.springer.com/article/10.1007/s11263-025-02507-2) · [Code](https://github.com/bociic/OCCO) |
| **OmniFuse** | 2025 · TPAMI | OmniFuse: Composite Degradation-Robust Image Fusion with Language-Driven Semantics | 文本引导 / 退化鲁棒 | — · [Code](https://github.com/HaoZhang1018/OmniFuse) |
| **PGMR** | 2025 · TCSVT | Plug-and-Play General Image Registration for Misaligned Multi-Modal Image Fusion | 配准 | [Paper](https://ieeexplore.ieee.org/document/11005625) · [Code](https://github.com/stwts/PGMR) |
| **ReferenceSupervisionIVIF** | 2025 · Pattern Recognition | Reference-then-Supervision Framework for Infrared and Visible Image Fusion | 伪监督 | [Paper](https://doi.org/10.1016/j.patcog.2024.110996) · [Code](https://github.com/zhenglab/ReferenceSupervisionIVIF) |
| **RPFNet** | 2025 · ACM MM | Residual Prior-driven Frequency-aware Network for Image Fusion | 频域 / 互补信息 | [Paper](https://arxiv.org/abs/2507.06735) · [Code](https://github.com/wang-x-1997/RPFNet) |
| **SAGE** | 2025 · CVPR | Every SAM Drop Counts: Embracing Semantic Priors for Multi-Modality Image Fusion and Beyond | 语义先验 | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Every_SAM_Drop_Counts_Embracing_Semantic_Priors_for_Multi-Modality_Image_CVPR_2025_paper.html) · [Code](https://github.com/RollingPlain/SAGE_IVIF) |
| **SpTFuse** | 2025 · Pattern Recognition | SAM-guided multi-level collaborative Transformer for infrared and visible image fusion | 语义先验 | [Paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320325000512) · [Code](https://github.com/lxq-jnu/SpTFuse) |
| **SSDFusion** | 2025 · Pattern Recognition | SSDFusion: A scene-semantic decomposition approach for visible and infrared image fusion | 语义先验 | [Paper](https://doi.org/10.1016/j.patcog.2025.111457) · [Code](https://github.com/YiXian-Xiao/SSDFusion) |
| **TDFusion** | 2025 · CVPR | Task-driven Image Fusion with Learnable Fusion Loss | 任务驱动 / 可学习损失 | [Paper](https://arxiv.org/pdf/2412.03240) · [Code](https://github.com/HaowenBai/TDFusion) |
| **TextFusion** | 2025 · Information Fusion | TextFusion: Unveiling the Power of Textual Semantics for Controllable Image Fusion | 文本引导 / 可控融合 | [Paper](https://www.sciencedirect.com/science/article/abs/pii/S1566253524005682?casa_token=wIR2KSNJG6sAAAAA:TITMGkb8jaVZ9EDKYhxK5XhWMKok2k62RgFkldDQsjvI6EpTty4gvcHXR1Cq52AFsdsVOF9IDw) · [Code](https://github.com/AWCXV/TextFusion) |
| **TITA** | 2025 · ICCV | Balancing task-invariant interaction and task-specific adaptation for unified image fusion | 通用融合 / 自适应 / 多任务优化 | [Paper](https://arxiv.org/pdf/2504.05164) · [Code](https://github.com/huxingyuabc/TITA) |
| **EMMA** | 2024 · CVPR | Equivariant Multi-Modality Image Fusion | 等变性 / 自监督 | — · [Code](https://github.com/Zhaozixiang1228/MMIF-EMMA) |
| **IMF** | 2024 · TCSVT | Improving Misaligned Multi-modality Image Fusion with One-stage Progressive Dense Registration | 配准 | [Paper](https://arxiv.org/pdf/2308.11165) · [Code](https://github.com/wdhudiekou/IMF) |
| **ReFusion** | 2024 · IJCV | ReFusion: Learning Image Fusion from Reconstruction with Learnable Loss Via Meta-Learning | 元学习 / 可学习损失 / 重建学习 | [Paper](https://doi.org/10.1007/s11263-024-02256-8) · [Code](https://github.com/HaowenBai/ReFusion) |
| **Text-IF** | 2024 · CVPR | Text-IF: Leveraging Semantic Text Guidance for Degradation-Aware and Interactive Image Fusion | 文本引导 / 可控融合 / 退化鲁棒 | [Paper](https://arxiv.org/abs/2403.16387) · [Code](https://github.com/Linfeng-Tang/Text-IF) |
| **DRMF** | 2024 · ACM MM | DRMF: Degradation-Robust Multi-Modal Image Fusion via Composable Diffusion Prior | 扩散 / 退化鲁棒 | [Paper](https://doi.org/10.1145/3664647.3681064) · [Code](https://github.com/Linfeng-Tang/DRMF) |
| **CDDFuse** | 2023 · CVPR | CDDFuse: Correlation-Driven Dual-Branch Feature Decomposition for Multi-Modality Image Fusion. | 特征分解 / 相关性 | [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Zhao_CDDFuse_Correlation-Driven_Dual-Branch_Feature_Decomposition_for_Multi-Modality_Image_Fusion_CVPR_2023_paper.html) · [Code](https://github.com/Zhaozixiang1228/MMIF-CDDFuse) |
| **DDFM** | 2023 · ICCV | DDFM: Denoising Diffusion Model for Multi-Modality Image Fusion | 扩散 / 无监督 | [Paper](https://arxiv.org/abs/2303.06840) · [Code](https://github.com/Zhaozixiang1228/MMIF-DDFM) |
| **SegMiF** | 2023 · ICCV | Multi-interactive Feature Learning and a Full-time Multi-modality Benchmark for Image Fusion and Segmentation | 任务驱动 / 分割 | [Paper](https://arxiv.org/abs/2308.02097) · [Code](https://github.com/JinyuanLiu-CV/SegMiF) |
| **SeAFusion** | 2022 · Information Fusion | Image Fusion in the Loop of High-Level Vision Tasks: A Semantic-Aware Real-Time Infrared and Visible Image Fusion Network | 任务驱动 / 分割 | [Paper](https://www.sciencedirect.com/science/article/pii/S1566253521002542) · [Code](https://github.com/Linfeng-Tang/SeAFusion) |
| **TarDAL** | 2022 · CVPR | Target-Aware Dual Adversarial Learning and a Multi-Scenario Multi-Modality Benchmark to Fuse Infrared and Visible for Object Detection | 任务驱动 / 检测 / GAN | [Paper](https://arxiv.org/abs/2203.16220) · [Code](https://github.com/JinyuanLiu-CV/TarDAL) |
| **U2Fusion** | 2022 · TPAMI | U2Fusion: A Unified Unsupervised Image Fusion Network | 通用融合 / 无监督 | [Paper](https://doi.org/10.1109/TPAMI.2020.3012548) · [Code](https://github.com/hanna-xu/U2Fusion) |
| **SwinFusion** | 2022 · IEEE/CAA JAS | SwinFusion: Cross-domain Long-range Learning for General Image Fusion via Swin Transformer | Transformer / 通用融合 | [Paper](https://doi.org/10.1109/JAS.2022.105686) · [Code](https://github.com/Linfeng-Tang/SwinFusion) |
| **DenseFuse** | 2019 · TIP | DenseFuse: A Fusion Approach to Infrared and Visible Images | CNN / 自编码器 | [Paper](https://ieeexplore.ieee.org/document/8580578) · [Code](https://github.com/hli1221/imagefusion_densefuse) |
| **FusionGAN** | 2019 · Information Fusion | FusionGAN: A Generative Adversarial Network for Infrared and Visible Image Fusion | GAN | [Paper](https://www.sciencedirect.com/science/article/pii/S1566253518301143) · [Code](https://github.com/jiayi-ma/FusionGAN) |

<a id="medical"></a>
## 医学图像

| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题 | 论文 / 代码 |
| :-- | :-- | :-- | :-- | :-- |
| **Mask-DiFuser** | 2026 · TPAMI | Mask-DiFuser: A Masked Diffusion Model for Unified Unsupervised Image Fusion | 扩散 | [Paper](https://ieeexplore.ieee.org/document/11162636) · [Code](https://github.com/Linfeng-Tang/Mask-DiFuser) |
| **AU-Net** | 2025 · TIP | AU-Net: Adaptive Unified Network for Joint Multi-Modal Image Registration and Fusion | 配准 | [Paper](https://doi.org/10.1109/TIP.2025.3586507) · [Code](https://github.com/luming1314/AU-Net) |
| **BSAFusion** | 2025 · AAAI | BSAFusion: A Bidirectional Stepwise Feature Alignment Network for Unaligned Medical Image Fusion | 配准 | [Paper](https://doi.org/10.1609/aaai.v39i5.32499) · [Code](https://github.com/slrl123/BSAFusion) |
| **C2RF** | 2025 · IJCV | C2RF: Bridging Multi-modal Image Registration and Fusion via Commonality Mining and Contrastive Learning | 配准 | [Paper](https://doi.org/10.1007/s11263-025-02427-1) · [Code](https://github.com/QinglongYan-hub/C2RF) |
| **DM-FNet** | 2025 · TMM | DM-FNet: Unified Multimodal Medical Image Fusion via Diffusion Process-Trained Encoder-Decoder | 扩散 / 医学融合 | [Paper](https://doi.org/10.1109/TMM.2025.3613156) · [Code](https://github.com/HeDan-11/DM-FNet) |
| **GIFNet** | 2025 · CVPR | One Model for ALL: Low-Level Task Interaction Is a Key to Task-Agnostic Image Fusion | 通用融合 / 联合训练 | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Cheng_One_Model_for_ALL_Low-Level_Task_Interaction_Is_a_Key_CVPR_2025_paper.html) · [Code](https://github.com/AWCXV/GIFNet) |
| **MMIF-INet** | 2025 · Information Fusion | MMIF-INet: Multimodal medical image fusion by invertible network | 可逆网络 / 医学融合 | [Paper](https://doi.org/10.1016/j.inffus.2024.102666) · [Code](https://github.com/HeDan-11/MMIF-INet) |
| **UniFuse** | 2025 · ICCV | UniFuse: A Unified All-in-One Framework for Multi-Modal Medical Image Fusion Under Diverse Degradations and Misalignments | 配准 / 退化鲁棒 / Mamba | [Paper](https://arxiv.org/abs/2506.22736) · [Code](https://github.com/slrl123/UniFuse) |
| **EMMA** | 2024 · CVPR | Equivariant Multi-Modality Image Fusion | 等变性 / 自监督 | — · [Code](https://github.com/Zhaozixiang1228/MMIF-EMMA) |
| **TFS-Diff** | 2024 · MICCAI | Simultaneous Tri-Modal Medical Image Fusion and Super-Resolution using Conditional Diffusion Model | 扩散 / 三模态 / 超分辨率 | [Paper](https://papers.miccai.org/miccai-2024/703-Paper3901.html) · [Code](https://github.com/XylonXu01/TFS-Diff) |
| **DRMF** | 2024 · ACM MM | DRMF: Degradation-Robust Multi-Modal Image Fusion via Composable Diffusion Prior | 扩散 / 退化鲁棒 | [Paper](https://doi.org/10.1145/3664647.3681064) · [Code](https://github.com/Linfeng-Tang/DRMF) |
| **CDDFuse** | 2023 · CVPR | CDDFuse: Correlation-Driven Dual-Branch Feature Decomposition for Multi-Modality Image Fusion. | 特征分解 / 相关性 | [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Zhao_CDDFuse_Correlation-Driven_Dual-Branch_Feature_Decomposition_for_Multi-Modality_Image_Fusion_CVPR_2023_paper.html) · [Code](https://github.com/Zhaozixiang1228/MMIF-CDDFuse) |
| **DDFM** | 2023 · ICCV | DDFM: Denoising Diffusion Model for Multi-Modality Image Fusion | 扩散 / 无监督 | [Paper](https://arxiv.org/abs/2303.06840) · [Code](https://github.com/Zhaozixiang1228/MMIF-DDFM) |
| **U2Fusion** | 2022 · TPAMI | U2Fusion: A Unified Unsupervised Image Fusion Network | 通用融合 / 无监督 | [Paper](https://doi.org/10.1109/TPAMI.2020.3012548) · [Code](https://github.com/hanna-xu/U2Fusion) |
| **SwinFusion** | 2022 · IEEE/CAA JAS | SwinFusion: Cross-domain Long-range Learning for General Image Fusion via Swin Transformer | Transformer / 通用融合 | [Paper](https://doi.org/10.1109/JAS.2022.105686) · [Code](https://github.com/Linfeng-Tang/SwinFusion) |

<a id="general"></a>
## 通用融合

| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题 | 论文 / 代码 |
| :-- | :-- | :-- | :-- | :-- |
| **1D-Fusion** | 2026 · ICML | From 2D Grids to 1D Tokens: Reforming Shared Representations for Multimodal Image Fusion | 预训练Tokenizer / 一维表示 | [Paper](https://proceedings.mlr.press/v306/xian26b.html) · — |
| **DECC** | 2026 · CVPR | More Than Meets the Eye: A Unified Image Fusion Framework via Semantic-Pixel Entropy Trade-off for Zero-Shot Generalization | 通用融合 / 语义像素权衡 / 零样本 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_More_Than_Meets_the_Eye_A_Unified_Image_Fusion_Framework_CVPR_2026_paper.html) · [Code](https://github.com/XiaoW-Liu/DECC) |
| **ISFL** | 2026 · CVPR | Multi-Modal Image Fusion via Intervention-Stable Feature Learning | 干预稳定性 / 分布偏移 | [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Multi-Modal_Image_Fusion_via_Intervention-Stable_Feature_Learning_CVPR_2026_paper.html) · — |
| **Mask-DiFuser** | 2026 · TPAMI | Mask-DiFuser: A Masked Diffusion Model for Unified Unsupervised Image Fusion | 扩散 | [Paper](https://ieeexplore.ieee.org/document/11162636) · [Code](https://github.com/Linfeng-Tang/Mask-DiFuser) |
| **UniFusion** | 2026 · CVPR | UniFusion: A Unified Image Fusion Framework with Robust Representation and Source-Aware Preservation | 通用融合 / 表示学习 | [Paper](https://arxiv.org/abs/2603.14214) · [Code](https://github.com/dusongcheng/UniFusion) |
| **FS-Diff** | 2025 · Information Fusion | FS-Diff: Semantic guidance and clarity-aware simultaneous multimodal image fusion and super-resolution. | 扩散 / 超分辨率 / 语义先验 | — · [Code](https://github.com/XylonXu01/FS-Diff) |
| **Fusionbooster** | 2025 · IJCV | Fusionbooster: A unified image fusion boosting paradigm | 通用融合 | [Paper](https://arxiv.org/pdf/2305.05970) · [Code](https://github.com/AWCXV/FusionBooster) |
| **FusionINV** | 2025 · TIP | FusionINV: A Diffusion-Based Approach for Multimodal Image Fusion | 扩散 | [Paper](https://doi.org/10.1109/TIP.2025.3593775) · [Code](https://github.com/erfect2020/FusionINV) |
| **GIFNet** | 2025 · CVPR | One Model for ALL: Low-Level Task Interaction Is a Key to Task-Agnostic Image Fusion | 通用融合 / 联合训练 | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Cheng_One_Model_for_ALL_Low-Level_Task_Interaction_Is_a_Key_CVPR_2025_paper.html) · [Code](https://github.com/AWCXV/GIFNet) |
| **LFDT-Fusion** | 2025 · Information Fusion | LFDT-Fusion: A Latent Feature-guided Diffusion Transformer Model for General Image Fusion | 扩散 / Transformer / 潜空间 | [Paper](https://doi.org/10.1016/j.inffus.2024.102639) · [Code](https://github.com/BOYang-pro/LFDT-Fusion) |
| **MMAE** | 2025 · Pattern Recognition | MMAE: A universal image fusion method via mask attention mechanism | 通用融合 | [Paper](https://doi.org/10.1016/j.patcog.2024.111041) · [Code](https://github.com/xiangxiang-wang/MMAE) |
| **TITA** | 2025 · ICCV | Balancing task-invariant interaction and task-specific adaptation for unified image fusion | 通用融合 / 自适应 / 多任务优化 | [Paper](https://arxiv.org/pdf/2504.05164) · [Code](https://github.com/huxingyuabc/TITA) |
| **EMMA** | 2024 · CVPR | Equivariant Multi-Modality Image Fusion | 等变性 / 自监督 | — · [Code](https://github.com/Zhaozixiang1228/MMIF-EMMA) |
| **ReFusion** | 2024 · IJCV | ReFusion: Learning Image Fusion from Reconstruction with Learnable Loss Via Meta-Learning | 元学习 / 可学习损失 / 重建学习 | [Paper](https://doi.org/10.1007/s11263-024-02256-8) · [Code](https://github.com/HaowenBai/ReFusion) |
| **UAAFusion** | 2024 · TCSVT | Deep unfolding multi-modal image fusion network via attribution analysis | 深度展开 / 归因分析 | [Paper](https://arxiv.org/abs/2502.01467) · [Code](https://github.com/HaowenBai/UAAFusion) |
| **VDMUFusion** | 2024 · TIP | VDMUFusion: A Versatile Diffusion Model-Based Unsupervised Framework for Image Fusion | 扩散 / 通用融合 | [Paper](https://ieeexplore.ieee.org/abstract/document/10794610) · [Code](https://github.com/yuliu316316/VDMUFusion) |
| **CDDFuse** | 2023 · CVPR | CDDFuse: Correlation-Driven Dual-Branch Feature Decomposition for Multi-Modality Image Fusion. | 特征分解 / 相关性 | [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Zhao_CDDFuse_Correlation-Driven_Dual-Branch_Feature_Decomposition_for_Multi-Modality_Image_Fusion_CVPR_2023_paper.html) · [Code](https://github.com/Zhaozixiang1228/MMIF-CDDFuse) |
| **DDFM** | 2023 · ICCV | DDFM: Denoising Diffusion Model for Multi-Modality Image Fusion | 扩散 / 无监督 | [Paper](https://arxiv.org/abs/2303.06840) · [Code](https://github.com/Zhaozixiang1228/MMIF-DDFM) |
| **U2Fusion** | 2022 · TPAMI | U2Fusion: A Unified Unsupervised Image Fusion Network | 通用融合 / 无监督 | [Paper](https://doi.org/10.1109/TPAMI.2020.3012548) · [Code](https://github.com/hanna-xu/U2Fusion) |
| **SwinFusion** | 2022 · IEEE/CAA JAS | SwinFusion: Cross-domain Long-range Learning for General Image Fusion via Swin Transformer | Transformer / 通用融合 | [Paper](https://doi.org/10.1109/JAS.2022.105686) · [Code](https://github.com/Linfeng-Tang/SwinFusion) |
| **GFF** | 2013 · TIP | Image Fusion With Guided Filtering | 传统方法 / 引导滤波 | [Paper](https://doi.org/10.1109/TIP.2013.2244222) · — |

<a id="focus"></a>
## 多聚焦

| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题 | 论文 / 代码 |
| :-- | :-- | :-- | :-- | :-- |
| **CCSR-Net-Fusion** | 2025 · Information Fusion | Unfolding Coupled Convolutional Sparse Representation for Multi-Focus Image Fusion | 清晰度 / 多聚焦 | [Paper](https://www.sciencedirect.com/science/article/abs/pii/S1566253525000478) · [Code](https://github.com/yuliu316316/CCSR-Net-Fusion) |
| **DMANet** | 2025 · AAAI | Multi-Focus Image Fusion via Explicit Defocus Blur Modelling | 清晰度 / 多聚焦 | [Paper](https://doi.org/10.1609/aaai.v39i6.32714) · [Code](https://github.com/Tangzitao/DMANet) |
| **GIFNet** | 2025 · CVPR | One Model for ALL: Low-Level Task Interaction Is a Key to Task-Agnostic Image Fusion | 通用融合 / 联合训练 | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Cheng_One_Model_for_ALL_Low-Level_Task_Interaction_Is_a_Key_CVPR_2025_paper.html) · [Code](https://github.com/AWCXV/GIFNet) |
| **MMAE** | 2025 · Pattern Recognition | MMAE: A universal image fusion method via mask attention mechanism | 通用融合 | [Paper](https://doi.org/10.1016/j.patcog.2024.111041) · [Code](https://github.com/xiangxiang-wang/MMAE) |
| **TITA** | 2025 · ICCV | Balancing task-invariant interaction and task-specific adaptation for unified image fusion | 通用融合 / 自适应 / 多任务优化 | [Paper](https://arxiv.org/pdf/2504.05164) · [Code](https://github.com/huxingyuabc/TITA) |
| **U2Fusion** | 2022 · TPAMI | U2Fusion: A Unified Unsupervised Image Fusion Network | 通用融合 / 无监督 | [Paper](https://doi.org/10.1109/TPAMI.2020.3012548) · [Code](https://github.com/hanna-xu/U2Fusion) |
| **SwinFusion** | 2022 · IEEE/CAA JAS | SwinFusion: Cross-domain Long-range Learning for General Image Fusion via Swin Transformer | Transformer / 通用融合 | [Paper](https://doi.org/10.1109/JAS.2022.105686) · [Code](https://github.com/Linfeng-Tang/SwinFusion) |

<a id="exposure"></a>
## 多曝光

| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题 | 论文 / 代码 |
| :-- | :-- | :-- | :-- | :-- |
| **GIFNet** | 2025 · CVPR | One Model for ALL: Low-Level Task Interaction Is a Key to Task-Agnostic Image Fusion | 通用融合 / 联合训练 | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Cheng_One_Model_for_ALL_Low-Level_Task_Interaction_Is_a_Key_CVPR_2025_paper.html) · [Code](https://github.com/AWCXV/GIFNet) |
| **MMAE** | 2025 · Pattern Recognition | MMAE: A universal image fusion method via mask attention mechanism | 通用融合 | [Paper](https://doi.org/10.1016/j.patcog.2024.111041) · [Code](https://github.com/xiangxiang-wang/MMAE) |
| **TITA** | 2025 · ICCV | Balancing task-invariant interaction and task-specific adaptation for unified image fusion | 通用融合 / 自适应 / 多任务优化 | [Paper](https://arxiv.org/pdf/2504.05164) · [Code](https://github.com/huxingyuabc/TITA) |
| **MEFLUT** | 2023 · ICCV | MEFLUT: Unsupervised 1D Lookup Tables for Multi-exposure Image Fusion | LUT / 轻量化 | [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_MEFLUT_Unsupervised_1D_Lookup_Tables_for_Multi-exposure_Image_Fusion_ICCV_2023_paper.html) · [Code](https://github.com/Hedlen/MEFLUT) |
| **U2Fusion** | 2022 · TPAMI | U2Fusion: A Unified Unsupervised Image Fusion Network | 通用融合 / 无监督 | [Paper](https://doi.org/10.1109/TPAMI.2020.3012548) · [Code](https://github.com/hanna-xu/U2Fusion) |
| **SwinFusion** | 2022 · IEEE/CAA JAS | SwinFusion: Cross-domain Long-range Learning for General Image Fusion via Swin Transformer | Transformer / 通用融合 | [Paper](https://doi.org/10.1109/JAS.2022.105686) · [Code](https://github.com/Linfeng-Tang/SwinFusion) |
| **DeepFuse** | 2017 · ICCV | DeepFuse: A Deep Unsupervised Approach for Exposure Fusion With Extreme Exposure Image Pairs | CNN / 无监督 | [Paper](https://openaccess.thecvf.com/content_iccv_2017/html/Prabhakar_DeepFuse_A_Deep_ICCV_2017_paper.html) · — |

<a id="remote"></a>
## 遥感与高光谱

| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题 | 论文 / 代码 |
| :-- | :-- | :-- | :-- | :-- |
| **PMI-RFCoNet** | 2024 · TGRS | Progressive Multi-Iteration Registration-Fusion Co-Optimization Network for Unregistered Hyperspectral Image Super-Resolution | 配准 / 扩散 | [Paper](https://doi.org/10.1109/TGRS.2024.3408424) · [Code](https://github.com/Jiahuiqu/PMI-RFCoNet) |

<a id="video"></a>
## 视频融合

| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题 | 论文 / 代码 |
| :-- | :-- | :-- | :-- | :-- |
| **VideoFusion** | 2026 · CVPR | VideoFusion: A Spatio-Temporal Collaborative Network for Multi-modal Video Fusion | 时序一致性 / 恢复 | [Paper](https://arxiv.org/abs/2503.23359) · [Code](https://github.com/Linfeng-Tang/VideoFusion) |

<a id="assessment"></a>
## 融合质量评价

| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题 | 论文 / 代码 |
| :-- | :-- | :-- | :-- | :-- |
| **EVAFusion** | 2026 · CVPR | Bridging Human Evaluation to Infrared and Visible Image Fusion | 人类评价 / 奖励学习 | [Paper](https://arxiv.org/abs/2603.03871) · [Code](https://github.com/ALKA-Wind/EVAFusion) |
| **EvaNet** | 2026 · TPAMI | EvaNet: Towards More Efficient and Consistent Infrared and Visible Image Fusion Assessment | 学习型评价 | [Paper](https://ieeexplore.ieee.org/document/11477151) · [Code](https://github.com/AWCXV/EvaNet) |

<a id="related"></a>
## 相关工作（非双源像素融合）

| 方法 | 年份 · 发表 | 论文标题 | 技术 / 问题 | 论文 / 代码 |
| :-- | :-- | :-- | :-- | :-- |
| **MagicFuse** | 2026 · CVPR | MagicFuse: Single Image Fusion for Visual and Semantic Reinforcement | 模态缺失 / 知识迁移 | [Paper](https://arxiv.org/abs/2602.01760) · [Code](https://github.com/zhayanping/MagicFuse) |
| **IM-Fuse** | 2025 · MICCAI | IM-Fuse: Mamba-based Fusion Block for Brain Tumor Segmentation with Incomplete Modalities | Mamba / 模态缺失 / 分割 | [Paper](https://papers.miccai.org/miccai-2025/0437-Paper0747.html) · [Code](https://github.com/AImageLab-zip/IM-Fuse) |
## 数据集 / Datasets

按任务整理常用及近年发布的数据集、评测基准。优先链接原作者或官方维护页面；不同数据集的配准、训练/测试划分及标注条件并不一致，使用时请查阅原始说明。

| 任务 | 数据集 | 年份 | 类型 / 特点 | 官方入口 |
| :-- | :-- | :-- | :-- | :-- |
| 红外与可见光 | TNO | — | 经典红外/可见光场景 | [Dataset](https://figshare.com/articles/dataset/TNO_Image_Fusion_Dataset/1008029) |
| 红外与可见光 | RoadScene | 2020 | 道路场景图像对 | [Dataset](https://github.com/hanna-xu/RoadScene) |
| 红外与可见光 | MSRS | 2022 | 多场景日夜图像对 | [Dataset](https://github.com/Linfeng-Tang/MSRS) |
| 红外与可见光 | M3FD | 2022 | 多场景，含目标检测标注 | [Dataset](https://github.com/JinyuanLiu-CV/TarDAL) |
| 红外与可见光 | LLVIP | 2021 | 低照度可见光与红外、行人标注 | [Dataset](https://bupt-ai-cz.github.io/LLVIP/) |
| 红外与可见光 | FMB | 2023 | 融合与语义分割基准 | [Dataset](https://github.com/JinyuanLiu-CV/SegMiF) |
| 红外与可见光 | MSIV | 2025 | 7,000 对配准图像，多场景；附可选检测标注入口 | [Dataset](https://github.com/Yzhijia/Multi-Scenary-Infrared-and-Visible-images-dataset) |
| 红外与可见光 | AWMM-100K | 2026 | 基于既有图像对的雨雾雪退化构建并含实拍数据；划分见官网 | [Project](https://ixilai.github.io/AWMM-100K/) |
| 红外与可见光 | VIFB | 2020 | 经典红外可见光融合评测基准，21 对测试图像 | [Benchmark](https://github.com/xingchenzhang/VIFB) |
| 医学图像 | Whole Brain Atlas (Harvard) | — | 脑部多模态图像资源；使用时核对对应切片 | [Dataset](https://www.med.harvard.edu/AANLIB/home.html) |
| 医学图像 | IXI | — | T1/T2/PD 等脑 MRI；原始数据并非直接配准的融合测试对 | [Dataset](https://brain-development.org/ixi-dataset/) |
| 医学图像 | BraTS | — | 多序列脑肿瘤 MRI；原任务为分割，非专用融合基准 | [Dataset](https://www.med.upenn.edu/cbica/brats/) |
| 多聚焦 | Lytro | — | 经典多焦点摄影数据 | [Collection](https://github.com/xingchenzhang/MFIFB) |
| 多聚焦 | MFIFB | 2020 | 多聚焦方法比较与评测基准 | [Benchmark](https://github.com/xingchenzhang/MFIFB) |
| 多聚焦 | LMIF | 2025 | 229 对手机采集多焦点图像；含原始及预处理版本 | [Dataset](https://github.com/cvmdsp/LMIF) |
| 多曝光 | SICE | 2018 | 多曝光序列与融合评价 | [Project](https://github.com/csjcai/SICE) |
| 多曝光 | MEFB | 2021 | 多曝光融合方法比较与评测基准 | [Benchmark](https://github.com/xingchenzhang/MEFB) |
| 跨任务 | VLF | 2024 | 基于既有融合数据集的视觉语言描述扩展，不是新采集图像对 | [Dataset](https://github.com/Zhaozixiang1228/IF-FILM) |
| 视频融合 | M3SVD | 2025 | 220 对同步红外可见光视频；目前公开测试集，完整数据需联系作者 | [Dataset](https://github.com/Linfeng-Tang/M3SVD) |
| 视频融合 | VF-Bench | 2025 | 跨红外可见光、多曝光、多聚焦、医学的视频融合评测集合 | [Benchmark](https://github.com/Zhaozixiang1228/VF-Bench) |

## 收录与贡献

重点收录 CVPR、ICCV、ECCV、NeurIPS、ICML、AAAI、MICCAI、ACM MM，以及 TPAMI、TIP、IJCV、TMM、TCSVT、Information Fusion、Pattern Recognition、TGRS 的相关论文；少量重要代表作可作为期刊范围例外收录。

欢迎通过 Issue 或 PR 补充遗漏论文、修正分类或更新代码链接。请附上论文标题、发表渠道、年份和原文或作者代码链接。

Acknowledgements: Thanks to the maintainers of [IVIF_ZOO](https://github.com/RollingPlain/IVIF_ZOO) for their work on image fusion literature and datasets.
