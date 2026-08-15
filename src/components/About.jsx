export default function About({ data }) {
  const { profile, coreSkills, labels } = data;

  return (
    <section className="section" id="about">
      <h2>{labels.about}</h2>
      <p className="about__summary">{profile.summary}</p>

      <div className="chips">
        {coreSkills.map((skill) => (
          <span className="chip" key={skill}>
            {skill}
          </span>
        ))}
      </div>
    </section>
  );
}
