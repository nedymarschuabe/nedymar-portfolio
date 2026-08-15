export default function Education({ data }) {
  const { education, certifications, labels } = data;

  return (
    <section className="section" id="education">
      <h2>{labels.education}</h2>

      <div className="grid-two">
        <div>
          <h3 className="subheading">{labels.academicEducation}</h3>
          <ul className="plain-list">
            {education.map((item) => (
              <li key={item.school}>
                <strong>{item.school}</strong>
                <span>{item.degree}</span>
                <span className="muted">{item.period}</span>
              </li>
            ))}
          </ul>
        </div>

        <div>
          <h3 className="subheading">{labels.certifications}</h3>
          <ul className="plain-list">
            {certifications.map((cert) => (
              <li key={cert}>{cert}</li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
}
