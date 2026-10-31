# humanizer-linkedin

**Humanize LinkedIn drafts without changing what they mean.**

An open Agent Skill by **Loubak Francis Fequet**, AI consultant and trainer in Djibouti.

[Download the ready-to-import ZIP](https://github.com/LoubakInnovations/humanizer-linkedin/releases/download/v1.0.0/humanizer-linkedin-v1.0.0.zip) · [Inspect SKILL.md](SKILL.md) · [Lire en français](#version-française) · [About the author](#author)

`Agent Skills` · `English and French` · `No skill-specific API key` · `MIT`

Humanizer LinkedIn edits an existing draft in three passes: identify the tells, rewrite the post, then report every meaningful change. It aims for a natural personal voice without inventing facts, anecdotes, statistics or results.

## Before and after

Fictional example for demonstration only. It makes no performance claim.

**Before**

```text
Here's the thing.

Let's be honest, this tool could reduce turnaround time by 20%, if the data is complete.

Comment TRAINING to receive the programme.

Agree? Thoughts? #success
```

**After**

```text
A possible 20% gain.

This tool could reduce turnaround time by 20%, if the data is complete.

Comment TRAINING to receive the programme.
```

The number, condition and useful call to action remain. The throat-clearing, performative honesty and empty requests for comments are removed.

## What the skill does

| Pass | Work | Output |
| --- | --- | --- |
| Find the tells | Inspect rhetorical habits, repetition, generic vocabulary and feed formatting | A diagnosis based on exact excerpts |
| Rewrite | State the claim, sharpen the hook and match the available voice | A post ready to paste |
| Report | Explain replacements and anything deliberately retained | A change table and an honest editorial verdict |

- Preserves facts, numbers, names, links, qualifications and uncertainty
- Never stretches a short hook just to add detail
- Matches two or three personal writing samples when supplied
- Removes French quotation marks from the final post without deleting the enclosed words
- Avoids em dashes in editable prose
- Keeps useful calls to action and relevant hashtags
- Leaves an already clean draft unchanged

These punctuation choices are editorial preferences, not proof that a text was AI-generated. A fidelity exception is reported when a character belongs to a protected literal such as a name or URL.

## Download or install

### Ready-to-import ZIP

**[Download humanizer-linkedin v1.0.0](https://github.com/LoubakInnovations/humanizer-linkedin/releases/download/v1.0.0/humanizer-linkedin-v1.0.0.zip)**

The archive contains one `humanizer-linkedin/` folder with `SKILL.md`, the editorial references, interface metadata and attribution. Import it into a product that supports custom skills, when that feature is available for your account. Menus and permissions vary by product and plan.

GitHub's **Code → Download ZIP** option downloads the complete repository, including the documentation and release-building tool.

### Skills CLI

```bash
npx skills add LoubakInnovations/humanizer-linkedin
```

This follows the install format documented by [Skills CLI](https://skills.sh/docs/cli). Installation and behaviour still need to be checked in the agent you use. Publication here does not imply certification by a vendor or directory.

### Manual use

Open [SKILL.md](SKILL.md), copy its instructions into your assistant, then add your draft. This is manual prompt use, not a skill installation, so automatic loading of reference files is not guaranteed.

## Usage

In ChatGPT, select the skill with `@` when it is available. In Codex, use `$humanizer-linkedin`. Other products may use a different invocation method.

```text
Use humanizer-linkedin to edit this draft.

My writing samples, optional:
[two or three examples]

My draft:
[your text]
```

The default response contains the clean post, a change table, any exceptions and one candid line about whether the result reads naturally. Add `Return only the final post` when you do not need the report.

## Scope and limitations

This skill edits text. It does not publish to LinkedIn, connect to an account or open links during a normal edit. It adds no executable script or external service to the editorial workflow.

It does not automatically fact-check the draft, certify human authorship, promise reach, clicks or SEO results, or guarantee an AI-detector score. Without writing samples, voice matching is inferred from the draft itself.

The package follows the [Agent Skills specification](https://agentskills.io/specification). Targeted tests were run in the design environment, but import and behaviour have not been tested in every product. Only submit text that you are allowed to process under the privacy rules of the product you use.

## Files

| Path | Purpose |
| --- | --- |
| `SKILL.md` | Skill instructions and trigger description |
| `references/cas-editoriaux.md` | Editorial cases for fidelity, punctuation, uncertainty and calls to action |
| `agents/openai.yaml` | Interface metadata for compatible hosts |
| `CITATION.cff` | Structured attribution |
| `LICENSE` | MIT licence |
| `dist/` | Versioned ZIP and SHA-256 checksum |
| `tools/build_release.py` | Reproducible ZIP builder using the Python standard library |

## Author

**Loubak Francis Fequet** is an AI consultant and trainer based in Djibouti and the founder of **Cabinet Loubak Innovations**. He helps professionals adopt artificial intelligence, learn through practical training and create assistants suited to their work.

He was ranked **the No. 1 LinkedIn creator in the Republic of Djibouti in 2025, across all categories**, according to the 2025 Favikon ranking as reported by the author on his [professional website](https://loubakinnovations.com/).

- [AI consulting and training](https://loubakinnovations.com/)
- [Loubak Francis Fequet on GitHub](https://github.com/LoubakInnovations)

The distinction concerns the creator. It is not a measure of this skill's effectiveness.

## Origin, reuse and contribution

This implementation was designed under the direction of Loubak Francis Fequet, with AI assistance, from a brief supplied under the title *The LinkedIn Post Humaniser Prompt*. The original author of that brief was not independently identified. This version formalises the workflow, supports French and English, and adds fidelity rules and editorial edge cases.

The repositories studied for presentation conventions are credited in [docs/presentation-references.md](docs/presentation-references.md). Their authors are not associated with this project and have not endorsed it.

The [MIT licence](LICENSE) allows reuse and modification with the notice retained. To report a problem, provide an anonymised example, the observed output and the expected behaviour. Do not publish confidential data in an issue.

---

## Version française

**Humanisez vos brouillons LinkedIn sans changer leur sens.**

Un skill ouvert de **Loubak Francis Fequet**, consultant et formateur en intelligence artificielle à Djibouti.

[Télécharger le ZIP prêt à importer](https://github.com/LoubakInnovations/humanizer-linkedin/releases/download/v1.0.0/humanizer-linkedin-v1.0.0.zip) · [Lire SKILL.md](SKILL.md) · [Revenir à l'anglais](#humanizer-linkedin) · [Découvrir l'auteur](#auteur)

Humanizer LinkedIn révise un brouillon en trois passes : repérer les tics, réécrire le post, puis rendre compte de chaque modification utile. Il vise une voix personnelle et naturelle sans inventer de faits, d'anecdotes, de statistiques ou de résultats.

### Avant et après

Exemple fictif, fourni uniquement pour illustrer le traitement attendu.

**Avant**

```text
Voici le truc.

Soyons honnêtes, cet outil pourrait réduire le délai de 20 %, si les données sont complètes.

Pour recevoir le programme, écrivez FORMATION.

D'accord ? Vos avis ? #success
```

**Après**

```text
Un gain possible de 20 %.

Cet outil pourrait réduire le délai de 20 %, si les données sont complètes.

Pour recevoir le programme, écrivez FORMATION.
```

Le chiffre, la condition et l'appel à l'action utile sont conservés. Le préambule, la sincérité de façade et les demandes vides de commentaires disparaissent.

### Ce que fait le skill

| Passe | Travail | Résultat |
| --- | --- | --- |
| Repérage | Examiner les tics rhétoriques, les répétitions, le vocabulaire générique et la mise en forme | Un diagnostic fondé sur les passages exacts |
| Réécriture | Poser l'idée, affûter l'accroche et respecter la voix disponible | Un post prêt à copier |
| Bilan | Expliquer les remplacements et ce qui a volontairement été conservé | Un tableau et une appréciation éditoriale honnête |

- Conserve les faits, chiffres, noms, liens, réserves et conditions
- Ne rallonge jamais une accroche courte pour ajouter des précisions
- S'adapte à deux ou trois publications personnelles si vous les fournissez
- Retire les guillemets français du post final sans supprimer les mots encadrés
- Évite les tirets cadratins dans la prose éditable
- Conserve les appels à l'action utiles et les hashtags pertinents
- Ne modifie pas un brouillon déjà propre

Ces choix de ponctuation sont des préférences éditoriales, pas des preuves d'origine IA. Une exception de fidélité est signalée lorsqu'un caractère appartient à un élément littéral protégé, tel qu'un nom ou une URL.

### Télécharger ou installer

**[Télécharger humanizer-linkedin v1.0.0](https://github.com/LoubakInnovations/humanizer-linkedin/releases/download/v1.0.0/humanizer-linkedin-v1.0.0.zip)**

L'archive contient un seul dossier `humanizer-linkedin/` avec `SKILL.md`, les références éditoriales, les métadonnées d'interface et l'attribution. Importez-la dans une interface acceptant les skills personnalisés, si cette fonction est disponible sur votre compte.

Avec la CLI Skills :

```bash
npx skills add LoubakInnovations/humanizer-linkedin
```

Sans import de skill, ouvrez [SKILL.md](SKILL.md), copiez ses instructions dans votre assistant, puis ajoutez votre brouillon. Le chargement automatique des références n'est alors pas garanti.

### Utilisation

Dans ChatGPT, sélectionnez le skill avec `@` lorsqu'il est disponible. Dans Codex, utilisez `$humanizer-linkedin`. Les autres produits peuvent employer un autre mode d'invocation.

```text
Utilise humanizer-linkedin pour réviser ce brouillon.

Mes publications personnelles, facultatives :
[deux ou trois exemples]

Mon brouillon :
[votre texte]
```

Par défaut, la réponse contient le post, le tableau des modifications, les exceptions et une phrase honnête sur le naturel du résultat. Ajoutez `Rends uniquement le post final` si vous n'avez pas besoin du bilan.

### Périmètre et limites

Ce skill révise un texte. Il ne publie pas sur LinkedIn, ne se connecte pas au compte et ne consulte pas les liens pendant une révision normale. Il ne vérifie pas automatiquement les affirmations, ne certifie pas qu'un texte vient d'un humain et ne garantit ni portée, ni clics, ni SEO, ni résultat auprès d'un détecteur d'IA. Sans exemples personnels, la voix est approchée à partir du brouillon.

Le paquet suit la [spécification Agent Skills](https://agentskills.io/specification). Des essais ciblés ont été réalisés dans l'environnement de conception, mais l'import et le comportement n'ont pas été testés dans chaque produit.

### Auteur

**Loubak Francis Fequet** est consultant et formateur en intelligence artificielle à Djibouti, et fondateur du **Cabinet Loubak Innovations**. Il accompagne les professionnels dans l'adoption de l'IA, la formation pratique et la création d'assistants adaptés à leur travail.

Il a été classé **n° 1 des créateurs LinkedIn en République de Djibouti en 2025, toutes catégories confondues**, selon le classement Favikon 2025 communiqué par l'auteur sur son [site professionnel](https://loubakinnovations.com/).

- [Conseil et formations en intelligence artificielle](https://loubakinnovations.com/)
- [Loubak Francis Fequet sur GitHub](https://github.com/LoubakInnovations)

Cette distinction concerne le créateur. Elle ne mesure pas l'efficacité du skill.

### Origine, réutilisation et contribution

Cette implémentation a été conçue sous la direction de Loubak Francis Fequet, avec assistance IA, à partir d'un brief fourni sous le titre *The LinkedIn Post Humaniser Prompt*. L'auteur initial de ce brief n'a pas été identifié indépendamment. La présente version formalise le workflow, traite le français et l'anglais, et ajoute des règles de fidélité et des cas d'arbitrage.

Les dépôts étudiés pour les conventions de présentation sont crédités dans [docs/presentation-references.md](docs/presentation-references.md). Leurs auteurs ne sont pas associés au projet et ne l'ont pas approuvé.

La [licence MIT](LICENSE) autorise la réutilisation et la modification en conservant la notice. Pour signaler un problème, fournissez un exemple anonymisé, le résultat observé et le comportement attendu. Ne publiez pas de données confidentielles dans une issue.
